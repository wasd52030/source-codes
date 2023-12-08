using System.Net;
using System.Net.Sockets;
using System.Text;

string mcastAddr = "224.1.1.1";
int mcastPort = 5007;
int multicastTTL = 2;

IPAddress multicastAddress = IPAddress.Parse(mcastAddr);
IPEndPoint endPoint = new IPEndPoint(multicastAddress, mcastPort);

Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
socket.SetSocketOption(SocketOptionLevel.IP, SocketOptionName.MulticastTimeToLive, multicastTTL);

while (true)
{
    Thread.Sleep(1000);
    string message = $"WireShark Class, 許智程, C109152304";
    byte[] data = Encoding.UTF8.GetBytes(message);
    socket.SendTo(data, endPoint);
}