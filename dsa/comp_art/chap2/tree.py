# /usr/bin/env python
# coding:utf-8
'''
Created on May 9, 2014

@author: veb
'''
'''
describe tree
1.descrebe a company , department , staff
2.each node has a common name(not require unique);each node can only have max 2 sub node;node has details contains cn , level , parent
3.travel tree with 3 ways
4.search node with common name
5.search childrens with full path (level and cn or /../.../cn)
'''
def node(node_dict):
    pass
# root
root = dict()
root['cn'] = 'js'
root['level'] = 0
root['parent'] = ''
root['path'] = '/'.join((root['parent'], root['cn']))
print root, root.items() , root['cn']
