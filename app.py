from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)

def recommend_outfit(occasion, style, weather, body):

    # 🎓 COLLEGE + CASUAL
    if occasion == "college" and style == "casual":

        if weather == "hot":
            if body == "slim":
                return [
                    "Crop Top + Jeans",
                    "Oversized T-shirt + Cargo Pants",
                    "Traditional Kurti + Earrings"
                ]
            elif body == "curvy":
                return [
                    "Loose T-shirt + High Waist Jeans",
                    "Flowy Top + Straight Pants",
                    "Tunic + Leggings"
                ]

        elif weather == "cold":
            if body == "slim":
                return [
                    "Jeans + Hoodie",
                    "Fitted Outfit + Layers",
                    "Jacket + Top + Pants"
                ]
            elif body == "curvy":
                return [
                    "Long Sweater + Leggings",
                    "Hoodie + Straight Pants",
                    "Shirt + Jeans"
                ]

    # 🎓 COLLEGE + MODERN
    if occasion == "college" and style == "modern":

        if weather == "hot":
            if body == "slim":
                return [
                    "High Waist Jeans + Top",
                    "Tank Top + Skirt",
                    "T-shirt + Shorts"
                ]
            elif body == "curvy":
                return [
                    "High Waist Jeans + Tshirt",
                    "Wrap Top + Pants",
                    "Long Dress + Flats"
                ]

        elif weather == "cold":
            if body == "slim":
                return [
                    "Fitted Top + Jacket + Jeans",
                    "Sweater + High Waist Pants",
                    "Layered Outfit + Boots"
                ]
            elif body == "curvy":
                return [
                    "Long Coat + Top + Pants",
                    "Sweater + Straight Pants",
                    "Layered Kurti + Jeans"
                ]

    # 🎉 PARTY + MODERN
    if occasion == "party" and style == "modern":

        # 🌤 HOT WEATHER
        if weather == "hot":

            if body == "slim":
                return [
                    "Red Dress + Heels",
                    "Black Dress + Heels",
                    "Crop Top + Skirt"
            ]

            elif body == "curvy":
                return [
                    "Wrap Dress + Heels",
                    "A-line Dress + Belt",
                    "Jumpsuit + Heels"
            ]

    # ❄️ COLD WEATHER
    elif weather == "cold":

        if body == "slim":
            return [
                "Fitted Outfit + Layers",
                "Jacket + Dress + Boots",
                "Leather Jacket + Skirt"
            ]

        elif body == "curvy":
            return [
                "Long Coat + Dress",
                "Layered Dress + Jacket",
                "Jumpsuit + Jacket"
            ]
    # 🎉 PARTY + CASUAL
    if occasion == "party" and style == "casual":

        if weather == "hot":
            if body == "slim":
                return [
                    "Crop Top + Skirt",
                    "Cotton Dress + Sneakers",
                    "Denim Shorts + Cute Top"
                    ]
            elif body == "curvy":
                return [
                    "Flowy Dress + Sneakers",
                    "Loose Tshirt + Skirt",
                    "Black Jumpsuit + Accessories"
            ]

    elif weather == "cold":
        if body == "slim":
            return [
                "Sweater + Skirt",
                "Jacket + Jeans",
                "Hoodie + Mini Skirt"
            ]
        elif body == "curvy":
            return [
                "Long Sweater + Boots",
                "Jacket + Top + Pants",
                "Layered Dress + Blazer"
            ]

    
    
    # Sort
    sorted_outfits = sorted(outfit_scores, key=outfit_scores.get, reverse=True)

    return sorted_outfits[:3]

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    occasion = data['occasion']
    style = data['style']
    weather = data['weather']
    body = data['body']
    print("Weather:", weather)
    outfits = recommend_outfit(occasion, style, weather, body)
    return jsonify({"outfits": outfits})   

if __name__ == "__main__":
    app.run(debug=True)