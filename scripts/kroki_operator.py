import base64
import zlib

def test():
    x = "https://kroki.io/nomnoml/svg/eNpdj0EKgzAQRfc5RZZaULorWHHTVReF7kMWo0ZNiUYmE4rgQXqQXqn3qGKltjCLz5_35zPiqhFIjWpQJ-s7Svi5oxFBl0F47LUxUKsgHBnnIleApYwi0QOiJbnxkkxU1hveWk_N6_GUTDImUsgdIRSUXQDBlwplmkz5pVKyVUR8H8cH0WpXNFpV0-JmjRk65ZyMsi_-46Jv_y2nu3qazeGM72ZwJHCkZ2x5z911HYRbbpNdVfopeQOsIGfd"

    content = zlib.decompress(base64.urlsafe_b64decode(x.split("/")[-1])).decode('utf8')
    # print(content)
    encoded_cotnent = base64.urlsafe_b64encode(zlib.compress(content.encode('utf8'))).decode('utf8')
    print(encoded_cotnent)


if __name__ == "__main__":
    test()