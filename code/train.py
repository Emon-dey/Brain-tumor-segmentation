import torch
from config import args
from model import UNet3D
from brats20_dataset import BraTS20Dataset
from load_hyperparameters import hp


import numpy as np
def get_dataset(args, verbose=True):
	train_dataset = BraTS20Dataset(
		set_dir=hp["training_dir"],
		data_dir=hp["data_dir_name"],
		seg_dir=hp["seg_dir_name"])


	data_idcs = np.arange(len(train_dataset))
	clients_split = []
	length= int(len(train_dataset)/args.num_C) if args.data_length == 0 else args.data_length

	data = [train_dataset[data_idcs[j]] for j in range (length)]
	print(len(data_idcs))
	for i in range(args.num_C):
		np.random.shuffle(data_idcs)
		print(data_idcs)
		data = [train_dataset[data_idcs[j]] for j in range (length)]
		clients_split += [data]
	client_loaders = [torch.utils.data.DataLoader(x, batch_size=args.batch_size, shuffle=True, num_workers=2) for x in clients_split]
	return client_loaders
if __name__ == '__main__':
	torch.manual_seed(args.seed)
	
	# model = UNet3D(in_channels=args.in_channel, out_channels=args.output_channel).to(args.device)
	# client_loaders = get_dataset(args)