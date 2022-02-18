import os
import yaml
import requests
import sys

class XiaomiRomQuery:
    def __init__(self):
        rom_yaml_url = "https://cdn.jsdelivr.net/gh/XiaomiFirmwareUpdater/miui-updates-tracker@master/data/latest.yml"
        self.yaml_data = yaml.load(requests.get(rom_yaml_url).text,Loader=yaml.FullLoader)
        self.branch_map={"stable":"Stable","stable beta":"Stable Beta","beta":'Weekly',"public beta":'Public Beta'}
        self.method={"recovery":"Recovery","fastboot":"Fastboot",}
        self.codename={}
        for i in self.yaml_data:
            self.codename[i["codename"]] =""
        self.codename = sorted(list(self.codename.keys()))
        

    def query_rom(self,model_name,region,rom_cleases,rom_version):
        codename=self.query_codename(model_name,region)
        for item in self.yaml_data:
            if item["codename"] == codename and item["branch"]==self.branch_map[rom_version] and item["method"]==self.method[rom_cleases]:
                return item["link"]

    def query_codename(self,model_name,region):
        for i in self.codename:
            codename = model_name+"_"+region+"_global"
            if i == model_name and region=="cn":
               return model_name
            elif i == codename:
               return codename

        raise RuntimeError("Could not find {}".format(codename))

if __name__ == '__main__':
    region = "cn"
    rom_cleases = "recovery"
    rom_version = "beta"
    try:
        MODEL_NAME = str(sys.argv[1])
    except IndexError:
        print('\nUsage: XiaomiFirmwareUpdate.py <Device_Code>\n')
        print('    <Device_Code>: Device Code, eg. venus\n')
        try:
            input = raw_input
        except NameError: pass
        input('Press ENTER to exit...')
        sys.exit()

    xiaomiRomQuery = XiaomiRomQuery()
    # step 2: get rom link by query_rom()
    OutPut = xiaomiRomQuery.query_rom(MODEL_NAME,region,rom_cleases,rom_version)
    if OutPut == None:
        rom_version = "public beta"
        print(xiaomiRomQuery.query_rom(MODEL_NAME,region,rom_cleases,rom_version))
    else:
        print(OutPut)