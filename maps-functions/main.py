import os, requests
import functions_framework

@functions_framework.http
def maps_query(request):
    place = request.args.get("place", "")
    if not place:
        return {"error": "parametro 'place' requerido"}, 400

    resp = requests.get(
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json",
        params={
            "input": place,
            "inputtype": "textquery",
            "fields": "place_id,name,geometry,formatted_address",
            "key": "AIzaSyAhgnptNBfTfuSK0rkq6PYy38C9dInTvWI",
        }
    )
    return resp.json()