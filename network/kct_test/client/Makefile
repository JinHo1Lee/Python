include $(GW_SRC)/imds/include.mk

CXX = c++
CC  = gcc

OPT = -g -I$(GW_SRC)/lib -I$(GW_SRC)/imds/gw/common  -I$(GW_SRC)/imds/common/net -I$(GW_SRC)/imds/common -I$(GW_SRC)/imds/ibml -I$(GW_SRC)/imds/ibml/xerces/include -I$(MYSQL_INC) -I./KHUB_FREE_LIB -I./NGM_GPB_LIB -I$(GW_SRC)/smgpapi/trunk -I$(GW_SRC)/imds/gw/common/ngm -I$(GW_SRC)/imds/gw/common/ngm/morpt  -I$(GW_SRC)/imds/gw/common/Mt2Push -DIB_DEBUG_3 -DDB_MYSQL -I$(GW_SRC)/virtualCarrier/smts_virCarrier

LINKOPT = -L$(GW_SRC)/imds/common/net -lmmgp -L$(GW_SRC)/imds/gw/common -limdsgw -L$(GW_SRC)/imds/common -limds -L$(GW_SRC)/imds/ibml -libml -L$(GW_SRC)/imds/ibml/xerces/lib -lxerces-c -L$(GW_SRC)/lib -linfobank -L$(MYSQL_LIB) -lmysqlclient -L$(OPENSSL_LIB) -lcrypto

.SUFFIXES: .c .cpp .o

.cpp.o:
	$(CXX) $(OPT) -c $<

all : client

client : client.o
	$(CXX) client.o  $(LINKOPT) -o client

clean :
	rm -f server client *.o
