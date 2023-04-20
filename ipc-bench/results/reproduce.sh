#!/bin/bash -i

echo "100 B messages"
echo "----------------"
echo "domain:"
./build/source/domain/domain -c 500000 -s 100
echo "fifo:"
./build/source/fifo/fifo -c 500000 -s 100
echo "mmap:"
./build/source/mmap/mmap -c 5000000 -s 100
echo "mq:"
./build/source/mq/mq -c 200000 -s 100
echo "pipe:"
./build/source/pipe/pipe -c 200000 -s 100
echo "shm:"
./build/source/shm/shm -c 5000000 -s 100
echo "tcp:"
./build/source/tcp/tcp -c 100000 -s 100
echo "zeromq:"
./build/source/zeromq/zeromq -c 20000 -s 100

echo "10 kB messages"
echo "----------------"
echo "domain:"
./build/source/domain/domain -c 500000 -s 10000
echo "fifo:"
./build/source/fifo/fifo -c 500000 -s 10000
echo "mmap:"
./build/source/mmap/mmap -c 5000000 -s 10000
echo "mq:"
./build/source/mq/mq -c 200000 -s 10000
echo "pipe:"
./build/source/pipe/pipe -c 200000 -s 10000
echo "shm:"
./build/source/shm/shm -c 5000000 -s 10000
echo "tcp:"
./build/source/tcp/tcp -c 100000 -s 10000
echo "zeromq:"
./build/source/zeromq/zeromq -c 20000 -s 10000
