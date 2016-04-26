# SNMPwalk on Windows
# SnmpWalk.exe -r:10.40.0.1 -t:10 -c:"private" -os:1.3.6.1.2.1.2.2.1 -op:1.3.6.1.2.1.2.2.1.20
import snmp_helper

ip = '10.40.0.1'
a_user = 'mysnmpuser'
auth_key = 'myauthkey'
encrypt_key = 'myencryptkey'
snmp_user = (a_user, auth_key, encrypt_key)
my_router = (ip, 161)

systemName = '1.3.6.1.2.1.1.5.0'
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'
sysUptime = '1.3.6.1.2.1.1.3.0'

oid = ccmHistoryStartupLastChanged

snmp_data = snmp_helper.snmp_get_oid_v3(my_router, snmp_user, oid=oid)

output = snmp_helper.snmp_extract(snmp_data)
print output


if __name__ == '__main__':
    print "hello world"