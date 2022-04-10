from cryptography.hazmat.primitives import hashes, hmac
import hashlib

class StreamVideo:

    file_name: str = str()
    blocks: list
    hashed_blocks: list
    block_size = 1024

    def __init__(self, file_name):
        self.file_name = file_name
        self.blocks = []
        self.hashed_blocks = []

    def run(self, solution=None):

        print("************************************************")
        print(f"Encrypting: {self.file_name}")
        print("************************************************")

        block_number = 1
        with open(f"{self.file_name}", "rb") as file:

            for byte_block in iter(lambda: file.read(self.block_size),b""):
                self.blocks.append(byte_block)
                block_number += 1

        i = len(self.blocks) - 1
        hash = None
        while i >= 0 :
            sha256 = hashlib.sha256()
            byte_block = self.blocks[i]

            if hash:
                byte_block = byte_block + hash
            
            self.hashed_blocks.append(byte_block)
            sha256.update(byte_block)
            hash = sha256.digest()

            if i == 0:
                print("****************************************************************")
                _solution = hash.hex()
                print(_solution)

                if solution:
                    print("Compared to Solution", solution == _solution)

            i -= 1




if __name__ == "__main__":

    file_name = "example.mp4"
    example_solution = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"
    stream = StreamVideo(file_name)
    stream.run(solution=example_solution)


    file_name2 = "file.mp4"
    stream2 = StreamVideo(file_name2)
    stream2.run()

