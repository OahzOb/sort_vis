import random
import time
import subprocess
import platform

TIME_PER_STEP = 0.1

def clear():
    if platform.system() == 'Windows':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def clear_fake():
    print('\n' * 50)

class Target:
    def __init__(self, num_items: int = 30, min_val: int = 1, max_val: int = 50):
        self.num_items = num_items
        self.min_val = min_val
        self.max_val = max_val
        self._target = [random.randint(self.min_val, self.max_val) for _ in range(self.num_items)]
        self._frame = 0

    def __getitem__(self, idx):
        return self._target[idx]

    def __len__(self):
        return self.num_items

    def __str__(self):
        return str(self._target)

    def _print_status(self):
        clear()
        #clear_fake()
        self._frame += 1
        print(f'''Frame [{self._frame}]''')
        for height in range(self.max_val+1, 0, -1):
            bars = list()
            for val in self._target:
                if val < height:
                    if val == height - 1:
                        if val < 10:
                            bars.append(str(val) + ' ')
                        else:
                            bars.append(str(val))
                    else:
                        bars.append('  ')
                else:
                    bars.append('##')
            print('  '.join(bars))

    def swap(self, idx1, idx2):
        if max(idx1, idx2) >= self.num_items or min(idx1, idx2) < 0:
            raise ValueError("Swap idx out of range.")
        movement = abs(idx1 - idx2)
        if movement < 1:
            return
        idx = min(idx1, idx2)
        temp = self._target[idx]
        self._target[idx] = self._target[idx+1]
        self._target[idx+1] = temp
        self._print_status()
        time.sleep(TIME_PER_STEP)
        self.swap(idx+1, max(idx1, idx2))
        return

def pop_sort(target: Target):
    idx = 0
    length = len(target)
    has_popped = True
    while has_popped:
        has_popped = False
        for idx in range(length-1):
            if target[idx] > target[idx+1]:
                target.swap(idx, idx+1)
                has_popped = True
    return target


if __name__ == '__main__':
    target = Target()
    print(target)
    print(pop_sort(target))
