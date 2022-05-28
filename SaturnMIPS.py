import csv
shift = ['sll']
data_manip = ['sw', 'lw', 'sb']
branch = ['ble', 'beq']
li = ['li']
class Instruction():
    def __init__(self, mnemonic, form, opcode, func):
        self.mnemonic = mnemonic.strip()
        self.form = form
        self.opcode = f'{int(opcode, 16):0>6b}'
        if func == "x":
            self.func = f'{0:0>6b}'
        else:
            self.func =  f'{int(func, 16):0>6b}'
    
    def buildMachineCode(self):
        opcode = self.opcode
        func = self.func
        if self.form == 'r':
            rd_in = input("Input register destination: ")
            if self.mnemonic not in shift:
                rs_in = input("Input register source: ")
            else:
                rs_in = f'{0:0>5b}'
            rt_in = input("Input register to target: ")
            interface = f'{self.mnemonic} ${rd_in}, ${rs_in}, ${rt_in}'
            instruction = [rd_in, rs_in, rt_in, f'{0:0>5b}']
            for x, ins in enumerate(instruction):
                if ins[0] == '$':
                    ins = ins[1:0]
                instruction[x] = f'{int(ins):0>5b}'
            if self.mnemonic in shift:
                shamt_in = input("Input shift amount: ")
                instruction[3] = f'{int(shamt_in):0>5b}'
                interface = f'{self.mnemonic} ${rd_in},  ${rt_in}, {shamt_in}'
            concatbin = opcode + instruction[1] + instruction[2] + instruction[0] + instruction[3] + func
            print('size:' + str(len(concatbin)))
            print(instruction)
        if self.form == 'i':
            if self.mnemonic in branch:
                print("Branching!")
                rs_in = input("Input register source: ")
                rt_in = input("Input register to compare against: ") 
                imm_in = input("Input decimal immediate:")
                interface = f'{self.mnemonic} ${rs_in}, {rt_in}, {imm_in}'
            else:
                rt_in = input("Input register to target: ") 
                if self.mnemonic not in li:
                    rs_in = input("Input register source: ")
                else:
                    rs_in = f'{0:0>5b}'
                imm_in = input("Input decimal immediate:")
                interface = f'{self.mnemonic} ${rt_in}, ${rs_in}, {imm_in}'
            
            if self.mnemonic in data_manip:
                interface = f'{self.mnemonic} ${rt_in}, {imm_in}(${rs_in}) '

            instruction = [rt_in, rs_in, imm_in]
            for x, ins in enumerate(instruction):
                if ins[0] == '$':
                    ins = ins[1:0]
                if x == 2:
                    if (int(imm_in) < 0):
                        instruction[x] = bin(int(imm_in) % (1<<16))[2:] 
                    else:
                        instruction[x] = f'{int(imm_in):0>16b}'
                else:
                    instruction[x] = f'{int(ins):0>5b}'    
            concatbin = opcode + instruction[1] + instruction[0] + instruction[2]
            print('size:' + str(len(concatbin)))
            print(instruction)
        if self.form == 'j':
            address_in = input("Input line number in decimal: ")
            interface = f'{self.mnemonic} {address_in}'
            concatbin = opcode + f'{(((int(address_in)*4)>>2)-1):0>26b}'
        print()
        return hex(int(concatbin,2))[2:].rjust(8,'0'), interface

            

            

instructionDict = {}
with open('instruction_set.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row, data in enumerate(csv_reader):
        if row  == 0:
            continue
        else:
            print(data)
            instructionDict[data[0].strip()] = Instruction(data[0].strip(),data[1].strip(),data[2].strip(),data[3].strip())

for key in instructionDict:
    print(instructionDict[key].mnemonic)
    print(instructionDict[key].form)
    print(instructionDict[key].opcode)
    print(instructionDict[key].func)

while(1):
    print("Available instructions", end=":")
    print("Type exit to exit.")
    for key in instructionDict:
        print(key, end=" ")
    print("")
    try:
        x = input("Input mnemonic: ").strip()
        if x == "exit":
            break
        result, english = instructionDict[x].buildMachineCode()
        print(english + "  ("+result+")")
        
        with open("out.txt", 'a') as outfile:
            outfile.write(result + "\n")
        with open("out_eng.txt", 'a') as outfile:
            outfile.write(english + "\n")
        
    except Exception as e:
        print(e)


            