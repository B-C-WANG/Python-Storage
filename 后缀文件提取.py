import os
import shutil

def copy_all_with_suffix(dir,suffix):

    for i in os.walk(dir):
        base_dir = i[0]
        files = i[2]
        for file in files:
            if file.endswith(suffix):
                _from = base_dir+'/'+file
                _to_dir = "G:/wbc/GitHub/CRN_Run_Result/py_file/"+base_dir.replace("\\","/").split("G:/wbc/GitHub/CRN_Run_Result")[1]+"/"
                _to_file = _to_dir + "/" + file
                if not os.path.exists(_to_dir):
                        os.makedirs(_to_dir,exist_ok=True)

                shutil.copyfile(_from,_to_file)
if __name__ == '__main__':
    copy_all_with_suffix("G:\wbc\GitHub\CRN_Run_Result",
                         ".py")