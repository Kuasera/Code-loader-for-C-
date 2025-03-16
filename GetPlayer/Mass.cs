using System;
using System.Text;

namespace MainApp
{
	// Token: 0x02000003 RID: 3
	internal class Mass
	{
		// Token: 0x06000003 RID: 3 RVA: 0x00002064 File Offset: 0x00000264
		public static string Bike(string p1, string p2)
		{
			byte[] array = Convert.FromBase64String(p1);
			byte[] bytes = Encoding.UTF8.GetBytes(p2);
			int num = bytes.Length;
			int i = 0;
			int num2 = 0;
			while (i < array.Length)
			{
				byte[] array2 = array;
				int num3 = i;
				array2[num3] ^= (byte)((int)bytes[num2] + i % 20);
				i++;
				num2 = (num2 + 1) % num;
			}
			return Encoding.UTF8.GetString(array);
		}
	}
}
