# argparse.ArgumentParser
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b',
    '--basic',
    help="Mostra olá mundo na tela",
    # type=str,
    metavar='STRING',
    # default='olá mundo',
    required=False,
    # nargs='+',
    action='append',
)

parser.add_argument(
    '-v', '--verbose',
    help='Mostra Logs',
    action='store_true',
    required=False
)

args = parser.parse_args()

if args.basic is None:
    print('Nenhum valor passado para b')
    print(args.basic)
else:
    print(f'basic é {args.basic}')
