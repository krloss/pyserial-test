## Setup:

``` bash
pip install -t pip_modules/ -r requirements.pip
```

## Emulate serial port:
``` bash
sudo socat PTY,link=/dev/ttyS8 PTY,link=/dev/ttyS9
```

## Test:
``` bash
socat PTY,link=/tmp/tty1 PTY,link=/tmp/tty2
python read.py /tmp/tty1 8
python write.py /tmp/tty2 'test1234'
python read.py /tmp/tty1
```
