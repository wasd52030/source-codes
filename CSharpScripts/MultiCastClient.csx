using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

string mcastAddr = "224.1.1.1";
int mcastPort = 5007;
string bindAddr = "0.0.0.0";

IPAddress multicastAddress = IPAddress.Parse(mcastAddr);
IPEndPoint endPoint = new IPEndPoint(multicastAddress, mcastPort);

Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
socket.SetSocketOption(SocketOptionLevel.IP, SocketOptionName.AddMembership, new MulticastOption(multicastAddress));

socket.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReuseAddress, true);
socket.Bind(new IPEndPoint(IPAddress.Any, mcastPort));

byte[] buffer = new byte[1024];
EndPoint remoteEP = new IPEndPoint(IPAddress.Any, 0);

int bytesRead = socket.ReceiveFrom(buffer, ref remoteEP);
string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);

Console.WriteLine($"Server received from {remoteEP}\nmessage -> {message}");