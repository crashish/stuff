import os, io, sys, textwrap, re, urllib

parse_sig = re.compile(
            '\[(.*?)\]\s+?signature\s*=\s*(.*?)(\s+\?\?)*\s*ep_only\s*=\s*(\w+)(?:\s*section_start_only\s*=\s*(\w+)|)', re.S)
sig_f = urllib.urlopen('userdb.txt')
sig_data = sig_f.read()
sig_f.close()
sigs = parse_sig.findall(sig_data)
for packer_name, signature, superfluous_wildcards, ep_only, section_start_only in sigs:
        print packer_name
        print len(signature.replace(' ',''))/2
        print textwrap.fill(signature,48)
        print ''
