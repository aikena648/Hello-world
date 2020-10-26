import sys

num_steps = int(sys.argv[1])
fmt_template = '{}. {:>%d}' % num_steps

for x in range (1, num_steps +1):
    print (fmt_template.format(x, '#' * x))