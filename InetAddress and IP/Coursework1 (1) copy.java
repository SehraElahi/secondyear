/********************************************************************

Name: Sehra Elahi

Email: sc17s2e@leeds.ac.uk

Date: 02/0/2019

*********************************************************************/

import java.net.*;
import java.net.InetAddress;				// For InetAddress and UnknownHostException.
import java.io.*;										//For IOException
import java.util.ArrayList;
import java.util.Arrays;

// Class that uses java.net.InetAddress to convert hostname to IP Address, realting methods to features of IP
public class Coursework1 {

	// Arrays with IP bytes
	private ArrayList<String> ipArray1 = new ArrayList<>();
	private ArrayList<String> ipArray2 = new ArrayList<>();
	private ArrayList<String> ipArray3 = new ArrayList<>();
	private ArrayList<String> ipArray4 = new ArrayList<>();


	//getter method for sorting arrays with stored first IP bytes
	private ArrayList<String> getipArray1() {

		for ( int i = 1; i<ipArray1.size(); i++ ) {
			if ( ipArray1.get(0).equals(ipArray1.get(i)) ) {
					 ipArray1.set( i, ipArray1.get(0 ));
					}
			else { ipArray1.set( 0,"*" );
						 ipArray2.set( 0,"*" );
						 ipArray3.set( 0, "*" );
						 ipArray4.set( 0, "*" );
						 break;
					}
			}

		for( int i = 1; i<ipArray1.size(); i++ ) {
				ipArray1.set( i,"" );
		}

		return this.ipArray1;
 	}

//getter method for sorting arrays with stored second IP bytes
	private ArrayList<String> getipArray2() {

		for ( int i = 1; i<ipArray2.size(); i++ ) {
			if ( ipArray2.get(0).equals(ipArray2.get(i)) ) {
					 ipArray2.set( i, ipArray2.get(0 ));
					}
			else { ipArray2.set( 0,"*" );
						 ipArray3.set( 0, "*" );
						 ipArray4.set( 0, "*" );
						 break;
					}
			}

		for( int i = 1; i<ipArray2.size(); i++ ) {
				ipArray2.set( i,"" );
		}

		return this.ipArray2;
 	}

	//getter method for sorting arrays with stored third IP bytes
	private ArrayList<String> getipArray3() {

		for ( int i = 1; i<ipArray3.size(); i++ ) {
			if ( ipArray3.get(0).equals(ipArray3.get(i)) ) {
					 ipArray3.set( i, ipArray3.get(0 ));
					}
			else { ipArray3.set( 0,"*" );
						 ipArray4.set( 0, "*" );
						 break;
					}
			}

		for( int i = 1; i<ipArray3.size(); i++ ) {
				ipArray3.set( i,"" );
		}

		return this.ipArray3;
	}

	//getter method for sorting arrays with stored fourth IP bytes
	private ArrayList<String> getipArray4() {

		for ( int i = 1; i<ipArray4.size(); i++ ) {
			if ( ipArray4.get(0).equals(ipArray4.get(i)) ) {
					 ipArray4.set( i, ipArray4.get(0 ));
					}
			else { ipArray4.set( 0,"*" );
						 break;
					}
			}
		for( int i = 1; i<ipArray4.size(); i++ ) {
				ipArray4.set( i,"" );
		}

		return this.ipArray4;
 	}



	public void resolve( String host ) { //resolve method for instance of InetAddress
		try {
			InetAddress inet = InetAddress.getByName( host );

			System.out.println( "\nHost name : " + inet.getHostName() );
			System.out.println( "IP Address: " + inet.getHostAddress() );
			System.out.println( "Canonical Hostname: " + inet.getCanonicalHostName() );
			//timeout in milliseconds //isReachable to ping/check if an address is Reachable
			System.out.println( "Reachable: " + inet.isReachable(1000) );

			//IP is IPv6
			if ( inet instanceof Inet6Address ) {
				System.out.println( "IPv6" );
			}

			//IP is IPv6
			else if ( inet instanceof Inet4Address ) {
				System.out.println( "IPv4" );

				//split the IP into bytes and store into the array
		 		String[] tokens = inet.getHostAddress().split( "[.]" );
		 		ipArray1.add( tokens[0] );
		 		ipArray2.add( tokens[1] );
		 		ipArray3.add( tokens[2]) ;
		 		ipArray4.add( tokens[3] );
			}
	}

	catch( UnknownHostException  e )	{ 		// If an exception was thrown, echo to stdout.
		e.printStackTrace();							//printStackTrace is a method to see where the exception occurs
	}

	catch ( IOException e )	{
		e.printStackTrace();
	}

}


	public static void main( String[] args ) {  //main method, args is command line argument

			Coursework1 coursework1 = new Coursework1();
			for( int i = 0; i < args.length; i++ ) { //loop through the commond line arguments
					coursework1.resolve( args[i] ); //object resolve instance
			}

				// convert ArrayList to string and ammend to get desired output
				String result = Arrays.toString( coursework1.getipArray1().toArray()).replace("[", "").replace("]", "").replace(",", "").replace(" ", "" );

				String result2 = Arrays.toString( coursework1.getipArray2().toArray()).replace("[", "").replace("]", "").replace(",", "").replace(" ", "" );

				String result3 = Arrays.toString( coursework1.getipArray3().toArray()).replace("[", "").replace("]", "").replace(",", "").replace(" ", "" );

				String result4 = Arrays.toString( coursework1.getipArray4().toArray()).replace("[", "").replace("]", "").replace(",", "").replace(" ", "" );

				//print out concatenation of the strings
				System.out.println( "\n" + result + "." + result2 + "." + result3+ "." + result4 );
	}
}
