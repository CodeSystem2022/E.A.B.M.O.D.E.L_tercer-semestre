import logging
from DDBB import connect_DDBB
from FOOD import TransformAndLoad



logging.basicConfig(filename='scripts/DDBB.log',
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d - %m - %Y')

def main():
    TransformAndLoad()

if __name__ == '__main__':
    main()