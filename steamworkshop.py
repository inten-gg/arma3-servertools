import requests

class SteamWorkshop:

    def get_collection_item_ids(self, collection_id: int) -> list[int]:
        collection_response = requests.post('https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/', data='collectioncount=1&publishedfileids%5B0%5D={}'.format(collection_id), headers={ 'content-type': 'application/x-www-form-urlencoded' }).json()

        ids = []
        for item in collection_response['response']['collectiondetails'][0]['children']:
            ids.append(item['publishedfileid'])

        return ids
