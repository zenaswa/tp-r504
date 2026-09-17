public class MonProg
{
	public static void main( String[] args )
	{
		try{
			System.out.println( "nb args=" + args.length );
			for ( int i=0; i<args.length; i++){System.out.println(" arg " + i + "=" + args[i]);}
		}
		catch( Exception ex )
		{
			System.out.println("erreur ");
			ex.printStackTrace();
		}
	}

}
