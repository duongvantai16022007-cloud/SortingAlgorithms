import numpy as np
import os
class DatasetManager:
    def __init__(self, size=1_000_000, folder_name="data"):
        self.size = size
        self.folder_name = folder_name
        self.data_dict = {}
        self._create_folder()
    def _create_folder(self):
        os.makedirs(self.folder_name)
    def generate(self):
        self.data_dict['file_01.txt'] = np.sort(np.random.uniform(0, 1e8, self.size))
        de_data = np.random.uniform(0, 1e8, self.size)
        self.data_dict['file_02.txt'] = np.sort(de_data)[::-1]
        for i in range(3, 6):
            self.data_dict[f'file_{i:02d}.txt'] = np.random.uniform(0, 1e8, self.size)
        for i in range(6, 11):
            self.data_dict[f'file_{i:02d}.txt'] = np.random.randint(0, 1e8, self.size)

    def save(self):
        for filename, array in self.data_dict.items():
            path = os.path.join(self.folder_name, filename)
            fmt = '%.6f' if 'float' in filename else '%d'
            np.savetxt(path, array, fmt=fmt)

manager = DatasetManager(size=1_000_000, folder_name="Data_create")
manager.generate()
manager.save()