# Justin is resting and enjoying 'not being kidnapped' in Paris,
# but unfortunately, local kidnappers grab him in the Louvre friday morning.
# Just before police raid a known hideout, a semi-coded text-message was
# intercepted from phone in hideout. Gang is known to use shifting Caesar ciphers,
# with a code-key somehow indicating each letter shift

# Police have no clue what to do...can you help and find Justin?
# You know the code for encrypting a regular non-shifting Caesar(below),
# but how to find the offsets?

psw, intercepted_msg ='weshfrerot!elwiaojycqwfxbcbprrmabdhyviozepjpdgwfxbui'.split('!')
gpsw = psw * (len(intercepted_msg) // len(psw))
dd = len(intercepted_msg) - len(gpsw)
if dd > 0:
    gpsw += psw[:dd]
    
dbm = list(zip(intercepted_msg, gpsw))

msg = ''.join([chr((ord(v[0]) - ord(v[1]) -97) %26 + 97) for v in dbm])

print(msg)