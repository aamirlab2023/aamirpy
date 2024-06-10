from colorama import Fore, Style

def box(mol2_file, atom_types_file=None, charge_file=None, x_start=0, y_start=0, z_start=0, x_rep=1, y_rep=0, z_rep=0):

    with open(mol2_file, mode="r") as mol_info:
        mol2_lines = mol_info.readlines()
    mol_info.close()

    print(f'Counting number of atoms and bonds in {mol2_file:s}', end="...")
    n_atoms = int(mol2_lines[2].split()[0])
    n_bonds = int(mol2_lines[2].split()[1])
    print("[" + Fore.GREEN + "DONE" + Style.RESET_ALL +"]")
    print(f'{n_atoms:d} atoms and {n_bonds:d} bonds found')
    print(f'Looking up atoms and bonds section in {mol2_file:s}', end="...")
    counter = 0
    for mol2_line in mol2_lines:
        mol2_line = mol2_line.split()
        if mol2_line == ['@<TRIPOS>ATOM']:
            atoms_section = counter
        elif mol2_line == ['@<TRIPOS>BOND']:
            bonds_section = counter
        counter += 1
    print("[" + Fore.GREEN + "DONE" + Style.RESET_ALL + "]")
    print(f'Atoms section is starting at line {atoms_section:d}')
    print(f'Bonds section is starting at line {bonds_section:d}')

    x_coord = []
    y_coord = []
    z_coord = []
    charge = []
    for i in range(atoms_section + 1, bonds_section):
        x_coord.append(float(mol2_lines[i].split()[-7]))
        y_coord.append(float(mol2_lines[i].split()[-6]))
        z_coord.append(float(mol2_lines[i].split()[-5]))
        charge.append(mol2_lines[i].split()[-1])

    with open(atom_types_file, mode="r") as atom_types_file:
        atom_types_lines = atom_types_file.readlines()
    atom_types_file.close()

    for atom_types_line in atom_types_lines:
        atom_types_line = atom_types_line.split()
        print(atom_types_line)

    x_min = min(x_coord)
    y_min = min(y_coord)
    z_min = min(z_coord)

    x_coord = [i - x_min for i in x_coord]
    y_coord = [i - y_min for i in y_coord]
    z_coord = [i - z_min for i in z_coord]
    
    
# -7
# -6
# -5


box("ethanol_eem.mol2", atom_types_file= "atom_types.txt")
