import os
from description import get_description
from uniqueness import make_unique

directory ="./videos/"

def main():
    for file in os.listdir(directory):
        path_to_video = os.path.join(directory,file)
        description = get_description(path_to_video)
        uniquilize = make_unique(path_to_video, description)
        

if __name__ == "__main__":
    main()
