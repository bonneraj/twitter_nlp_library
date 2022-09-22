import logging
import os

# set up logging capability
def logger():
    '''
    Function to create/update log file after each run
    '''
    logging_file_path = 'log_output/execution_log.txt'
    if os.path.exists(logging_file_path):
        os.remove(logging_file_path)
    elif not os.path.isdir(logging_file_path.split('/')[0]):
        os.mkdir(logging_file_path.split('/')[0])
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(
        filename=logging_file_path,
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)-5s - %(message)-s',
        datefmt="%Y%m%d %H:%M:%S %p"
    )

    LOGGER = logging.getLogger(__name__)
    return LOGGER