

def is_equivalent(s1, s2):
    print(s1)
    print(s2)
    if len(s1) != len(s2):
	    return False
    relationships = {}
    comparison_string = []    
    for i in range(len(s1)):
        relationships[s1[i]] = s2[i]
    for i in range(len(s1)):
        comparison_string.append(relationships[s1[i]])
    comparison_string = "".join(comparison_string)
    print(comparison_string)
    return comparison_string == s2

print(is_equivalent("dadd", "boiib"))