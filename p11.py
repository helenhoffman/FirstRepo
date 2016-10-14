# ThinkPython2 Chapter 11 Directory

def invert_dict(d):
    invert = dict()
    for key in d:
        val = d[key]
	if val in inverse:
            inverse[val].append(key)
	else:
	    inverse[val] = [key]
    return inverse

invert_dict('append')
