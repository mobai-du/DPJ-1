#$_$ coding:utf-8 $_$
#__author__:Peter Du

import logging

# logging.warning("user [alex] attempted wrog password more than 3 times")
# logging.critical("server is down")

logging.basicConfig(filename="log_test.log",
                    level=logging.CRITICAL,
                    format='%(asctime)s:%(levelname)s:%(message)s:%(pathname)s:%(filename)s',
                    datefmt='%y--%m--%d %H:%M:%S %p %a-%A %b-%B %c'
                            '%j %U %w %W %x %X %z %%')

logging.debug("This message is Debug")
logging.info("This message is INFO")
logging.warning("This message is warning")
logging.error("This message is error")
logging.critical("This message is critical")
logging.critical("This message is critical")
logging.critical("This message is critical")
logging.critical("This message is critical")
logging.critical("This message is critical")

#TODO 我突然有个好点子