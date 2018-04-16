from initialize_database import *
from clarifai import rest
from clarifai.rest import ClarifaiApp

from plotly.offline import plot
import plotly.graph_objs as go

API_KEY = "ENTER-YOUR-API-KEY"

def main():

    while (True):
        user_choice = input("1. Process the Database (Add Tags for Products.\n2. Create Pie Charts.\n3. Exit.\n")

        if user_choice == 1:
            process_database()

        elif user_choice == 2:
            create_pie_chart()

        elif user_choice == 3:
            break

        else:
            print("Invalid Option.\nPlease Try Again.")

def process_database():
    app = ClarifaiApp(api_key=API_KEY)
    general_model = app.models.get("general-v1.3")
    logo_model = app.models.get('logo')
    color_model = app.models.get('color')

    product_query = Products.select()

    for product in product_query:
        print(product.product_id)
        tag_query = Tags.select().where(Tags.product_id == product.product_id)

        if len(tag_query) == 0:
            gen_response = general_model.predict_by_url(url=product.product_image)

            general_tag = add_general_tag(gen_response)


            logo_response = logo_model.predict_by_url(url=product.product_image)

            logo_tag = add_logo_tag(logo_response)


            color_response = color_model.predict_by_url(url=product.product_image)

            color_tag = add_color_tag(color_response)


            new_tag = Tags(product_id=product.product_id, general_tag=general_tag, logo_tag=logo_tag, color_tag=color_tag)
            new_tag.save()

def add_general_tag(response):
    if response["status"]["code"] == 10000:
        if len(response["outputs"][0]["data"]["concepts"]) > 0:
            tag_value = response["outputs"][0]["data"]["concepts"][0]["name"]
            return tag_value
    return None

def add_logo_tag(response):
    if response["status"]["code"] == 10000:
        if len(response["outputs"][0]["data"]["regions"]) > 0:
            if len(response["outputs"][0]["data"]["regions"][0]["data"]["concepts"]) > 0:
                tag_value = response["outputs"][0]["data"]["regions"][0]["data"]["concepts"][0]["name"]
                return tag_value
    return None

def add_color_tag(response):
    max_value = 0
    max_index = -1
    if response["status"]["code"] == 10000:
        if len(response["outputs"][0]["data"]["colors"]) > 0:
            for index in range(len(response["outputs"][0]["data"]["colors"])):
                if response["outputs"][0]["data"]["colors"][index]["value"] > max_value:
                    max_value = response["outputs"][0]["data"]["colors"][index]["value"]
                    max_index = index

            if max_index != -1:
                tag_value = response["outputs"][0]["data"]["colors"][max_index]["w3c"]["name"]
                return tag_value
    return None

def create_pie_chart():
    brands = {}
    colors = {}

    product_query = Products.select()

    for product in product_query:

        tag_query = Tags.select().where(Tags.product_id == product.product_id)

        if len(tag_query) > 0:

            brand_tag = tag_query[0].logo_tag
            color_tag = tag_query[0].color_tag

            if brand_tag in brands:
                brands[brand_tag] += 1
            else:
                brands[brand_tag] = 1

            if color_tag in colors:
                colors[color_tag] += 1
            else:
                colors[color_tag] = 1

    trace = go.Pie(labels=brands.keys(), values=brands.values())
    plot([trace], image='png', image_filename='Brands', filename='Brands.html')

    trace = go.Pie(labels=colors.keys(), values=colors.values())
    plot([trace], image='png', image_filename='Colors', filename='Colors.html')

main()