import kagglehub

DATASET = "olistbr/brazilian-ecommerce"
PATH = "./data"

kagglehub.dataset_download(DATASET, output_dir= PATH)