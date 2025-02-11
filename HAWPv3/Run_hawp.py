import os
import subprocess
import time

input_folder = r'/mnt/c/Users/sotas/TESTS/HAWP/hawp/datasets/dexi'
output_folder = r'/mnt/c/Users/sotas/TESTS/HAWP/hawp/docs/figures/dexi_out1111'  

for root, dirs, files in os.walk(input_folder):
    if files:  
        
        relative_path = os.path.relpath(root, input_folder)
        
        save_to = os.path.join(output_folder, relative_path)
        
        os.makedirs(save_to, exist_ok=True)
        
        img_path = os.path.join(root, '*.png')

        start_time = time.time()
        command = f'python -m hawp.ssl.predict --ckpt checkpoints/hawpv3-fdc5487a.pth --threshold 0.1 --img {img_path} --saveto {save_to} --ext json --t 0.1'

        
        process = subprocess.run(command, shell=True)
        
        end_time = time.time()

        total_time = end_time - start_time
        print(f"Η διαδικασία για τον φάκελο {root} ολοκληρώθηκε σε {total_time:.2f} δευτερόλεπτα.")

