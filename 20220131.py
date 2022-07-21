# Write code to handle admissions for a school
# Rules: pass test and interview. If applicant is legacy
# passing either test or interview is enough to be admitted.

appl = ['Jay', 'Sam', 'Vi', 'Li', 'My', 'Xi', 'On', 'Mo', 'An', 'Bo']
test_ok = ['xi', 'my', 'sam', 'an', 'mo', 'on']
int_ok = ['my', 'li', 'an', 'mo', 'bo', 'jay']
legacy = ['sue', 'bo', 'xi']

accepted = []

for x in test_ok:
    if x in int_ok:
        accepted.append(x)

for y in legacy:
    if (y in test_ok) or (y in int_ok):
        accepted.append(y)

print('Accepted students: ', end=' ')

for a in sorted([t for t in set(accepted)]):
    print(a.title(), end=', ')