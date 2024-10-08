# x = false, y = false
x = False
y = False
z = x and y
print("%r and %r = %r" % (x, y, z))

# x = false, y = true
x = False
y = True
z = x and y
print("%r and %r = %r" % (x, y, z))

# x = true, y = false
x = True
y = False
z = x and y
print("%r and %r = %r" % (x, y, z))

# x = true, y = true
x = True
y = True
z = x and y
print("%r and %r = %r" % (x, y, z))

# x = false, y = false
x = False
y = False
z = x or y
print("%r OR %r = %r" % (x, y, z))

# x = false, y = true
x = False
y = True
z = x or y
print("%r or %r = %r" % (x, y, z))

# x = true, y = false
x = True
y = False
z = x or y
print("%r or %r = %r" % (x, y, z))

# x = true, y = true
x = True
y = True
z = x or y
print("%r or %r = %r" % (x, y, z))

# x = false
x = False
y = not x
print("not %r = %r" % (x, y))

# x = true
x = True
y = not x
print("not %r = %r" % (x, y))
