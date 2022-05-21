import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--ada_thresh', type=bool,   default=True,       help= 'default True')
parser.add_argument('--T_thresh',   type=float,  default=0.05,       help= 'fixed threshold')
parser.add_argument('--lr',         type=float,  default=0.001,      help= 'learning rate')
parser.add_argument('--local_e',    type=int,    default=5,          help= 'local epoch')
parser.add_argument('--rounds',     type=int,    default=50,        help= 'global epoch')
parser.add_argument('--device',     type=str,    default='cuda:0',     help= 'GPU or not')
parser.add_argument('--batch_size', type=int,    default=1,         help= 'batch size')

parser.add_argument('--optimizer',  type=str,    default='Adam',     help= 'optimizer')

parser.add_argument('--frac',       type=float,  default=1,          help= 'participation ratio')
parser.add_argument('--num_C',      type=int,    default=5,          help= 'client number')
parser.add_argument('--Nc',         type=int,    default=10,         help= 'class number on clients')
parser.add_argument('--data_length',         type=int,    default=50,         help= 'data_length')
parser.add_argument('--iid',        type=bool,   default=True,       help= 'iid or not')

parser.add_argument('--seed',       type=int,    default=1234,       help= 'seed')

parser.add_argument('--in_channel',       type=int,    default=4,       help= 'input_channel')
parser.add_argument('--output_channel',       type=int,    default=4,       help= 'output_channel')


args = parser.parse_args()
