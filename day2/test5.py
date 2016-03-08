#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
obj = subprocess.Popen(['python'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


obj.stdin.write('print 1 \n')
obj.stdin.write('print 2 \n')
obj.stdin.write('print 3 \n')
obj.stdin.write('print 4 \n')
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_err = obj.stderr.read()
obj.stderr.close()

print cmd_out
print cmd_err

