import requests

def main():
    print("Welcome to Ubuntu Image Fetcher")
    print("A tool for mindfully collecting image from the web\n")

    image_url = input("Please enter the URL of the image: ")
    response = requests.get(image_url)
    response.raise_for_status()

    import os
   
    def create_directory():
        folder_name = "Fetched_Images"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Directory '{folder_name}' created successfully.")
        else:
            print(f"Directory '{folder_name}' already exists.")
            return folder_name
        

        def download_image(image_url, folder_name):
            try: 
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()

                # Check Content-Type header

                content_type = response.headers.get("Content-Type", "")
                if not content_type.startswith("image/"):
                    print(f"The URL does not point to an image. Content-Type: ")
                    return
                
                # Extract filename from URL

                filename = image_url.split("/")[-1] or "downloaded_image.jpg"
                filepath = os.path.join(folder_name, filename)

                # Save image in binary mode
                with open(filepath, "wb") as file:
                    file.write(response.content)

                    print(f"Image successfully saved in binary mode to: {filepath}")

            except requests.exceptions.RequestException as e:
                print(f"Error downloading image: {e}")
            except requests.exceptions.Timeout:
                print("Connection timed out. Please try again later.")
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except requests.exceptions.ConnectionError:
                print("Connection error. Check your internet or the URl.")
            except requests.exceptions.RequestException as err:
                print(f"An unexpected error occured: {err}")

                def main():
                    image_url = input("Enter the image URL: ").strip()
                    if not image_url.startswith("http"):
                        print("Invalid URL. Make sure it starts with http or https.")
                        return
            folder = create_directory()
            download_image(image_url, folder)

            if __name__ == "__main__":
             main()