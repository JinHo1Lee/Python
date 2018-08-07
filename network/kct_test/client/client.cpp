#include "JDKCT.h"

IBSocket sock;

void printMsg(char *buf)
{
	KCTHeader *header = (KCTHeader *)buf;

	if(!memcmp(header->packetType, pREQ_BIND, sizeof(header->packetType)))
	{
		KCTBind *bind = (KCTBind*)buf;
		printf("Bind : %.4s %.4s %c ", header->packetLen, header->packetType, header->rsltCode);
		printf("%s %s %c\n", bind->customID, bind->customPW);
	}
	else if(!memcmp(header->packetType, pRET_BIND, sizeof(header->packetType)))
	{
		KCTBindAck *bindAck = (KCTBindAck*)buf;
		printf("BindAck : %.4s %.4s %c %s\n", header->packetLen, header->packetType, header->rsltCode, bindAck->failCause);
	}
	else if(!memcmp(header->packetType, pREQ_LINE_CHECK, sizeof(header->packetType)))
	{
		printf("ping : %.4s %.4s %c\n", header->packetLen, header->packetType, header->rsltCode);
	}
	else if(!memcmp(header->packetType, pRET_LINE_CHECK, sizeof(header->packetType)))
	{
		printf("pong : %.4s %.4s %c\n", header->packetLen, header->packetType, header->rsltCode);
	}
	else if(!memcmp(header->packetType, pREQ_SMS_CDR, sizeof(header->packetType)))
	{
		MO *mo = (MO*)buf;
		printf("mo : %.4s %.4s %c", header->packetLen, header->packetType, header->rsltCode);
		printf("%s %s %s %s %s\n", mo->rDate, mo->orgAddr, mo->dstAddr, mo->callbackNo, mo->msg);
	}
	else
	{
		printf("%s\n", buf);
	}
}

void makebind(char *buf)
{
	KCTHeader header;
	KCTBind bind;

	memset(&header, 0x00, sizeof(KCTHeader));
	memset(&bind, 0x00, sizeof(KCTBind));

	sprintf(header.packetLen, "%d", sizeof(KCTBind));
	memcpy(header.packetType, pREQ_BIND, sizeof(header.packetType));
	header.rsltCode = RSLT_CODE_REQ;

	memcpy(&(bind.Header), &header, sizeof(KCTHeader));
	strcpy(bind.customID, "jino");
	strcpy(bind.customPW, "pwjino");

	memcpy(buf, &bind, sizeof(KCTBind));
}

void makeping(char *buf)
{
	KCTHeader header;
	KCTReqLineCheck ping;

	memset(&header, 0x00, sizeof(KCTHeader));
	memset(&ping, 0x00, sizeof(KCTReqLineCheck));

	sprintf(header.packetLen, "%d", sizeof(KCTReqLineCheck));
	memcpy(header.packetType, pREQ_LINE_CHECK, sizeof(header.packetType));
	header.rsltCode = RSLT_CODE_REQ;

	memcpy(buf, &header, sizeof(KCTReqLineCheck));
}

int main (int argc, char **argv)
{
	char buf [1024];
	int pingcnt =0;

	while (1)
	{
		if (sock.Connect("172.16.2.55", 9999))
			break;
	}

	memset(buf, 0x00, sizeof(buf));
	//makebind(buf);
	strcpy(buf, "hello");
	sock.Send(buf, sizeof(buf), 0);
	//sock.Send(buf, sizeof(KCTBind), 0);
	//printf ("%d\n", sizeof(KCTBind));
	printMsg(buf);

	memset(buf, 0x00, sizeof(buf));
	sock.Receive(buf, sizeof(buf));
	printMsg(buf);
/*
	while (pingcnt < 10)
	{
		memset(buf, 0x00, sizeof(buf));
		makeping(buf);
		sock.Send(buf, sizeof(buf), 0);
		printMsg(buf);

		memset(buf, 0x00, sizeof(buf));
		sock.Receive(buf, sizeof(buf));
		sock.Receive(buf, sizeof(buf));
		printMsg(buf);

		pingcnt++;
	}

	memset(buf, 0x00, sizeof(buf));
	sock.Receive(buf, sizeof(buf));
	if (strlen(buf)!=0)
		printMsg(buf);
*/

	sock.Close();
	return 0;
}
