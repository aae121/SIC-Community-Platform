import json


class handel_file_json:


    def adde(self,
            filename: str,
            info: dict):
        file = open(filename + ".json", "r", encoding='utf-8')
        data = json.load(file)
        file.close()
        data.append(info)
        file = open(filename + ".json", "w", encoding='utf-8')
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.close()

    def get_data(self, filename: str):
        with open(filename + ".json", "r", encoding='utf-8') as file:
            data = json.load(file)
        return data

    def update_data(self, filename: str, updated_user: dict):
        with open(filename + ".json", "r", encoding='utf-8') as file:
            data = json.load(file)

        for i, user in enumerate(data):
            if user["id"] == updated_user["id"]:
                data[i] = updated_user
                break
        with open(filename + ".json", "w", encoding='utf-8') as file:
            json.dump(data, file, indent=2)

    def delete_data(self, filename: str, deleted_user: dict):
        with open(filename + ".json", "r", encoding='utf-8') as file:
            data = json.load(file)

        data = [user for user in data if user["id"] != deleted_user["id"]]

        with open(filename + ".json", "w", encoding='utf-8') as file:
            json.dump(data, file, indent=2)
