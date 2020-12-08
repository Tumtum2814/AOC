import re

def parse_bag(bag):
  name, contents = re.match(r'^(.*) bags contain (.*)$', bag).groups()
  return (name, dict((c[1], int(c[0])) for c in re.findall('(\d+) (.+?) bag', contents)))

def recursive_parents(bags, bag_name):
  parents = set(parent_name for (parent_name, parent_contents) in bags.items() if bag_name in parent_contents)
  return reduce(lambda a, b: a.union(recursive_parents(bags, b)), parents, parents)

def num_recursive_children(bags, bag):
    return reduce(lambda a, (child, count): a + count * (1 + num_recursive_children(bags, bags[child])), bag.items(), 0)

if __name__ == '__main__':
  with open('7_input.txt') as f:
    bags = dict(parse_bag(l) for l in f.readlines())
  print 'part 1: %d ' % len(recursive_parents(bags, 'shiny gold'))
  print 'part 2: %d ' % num_recursive_children(bags, bags['shiny gold'])