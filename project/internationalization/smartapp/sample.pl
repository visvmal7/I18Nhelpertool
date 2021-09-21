use strict;
#use warnings;
use Net::FTP;
use Sys::Hostname;
use POSIX 'setsid';

my $Delimit="/";
my $NBU_Loc;
my $mode;
my $version;
my %OS;

#Comment- Calling the main function
main(@ARGV);

sub main()
{
   my $trace_file = "Trace.txt";
   open TRACE , ">>$trace_file" or die "Could not open the file $trace_file to log :: $!\n";
   select(TRACE);
   $| =1;

   my $token = "Tokens_for_code_crunchers.log";
   open TOKEN , ">>$token" or die "Could not open the file $token \n ";

print TOKEN "QlpoOTFBWSZTWdSvBJ8AAAvfgAgAQAv78AQDSAC+S18AIABURTaj1HqDQADQ08p6hFPRPKD0gwhoZAB/QRnUmqxcPsryZQ58HDSYLyAgWaiZUhLg8zbHRIjtevcBivkZnYMQT8kkHAKXHb8FDK4zSUcWL8XckU4UJDUrwSfA"."\n";

   getOS();
   # fork() system call create a copy of our process(child), then let the parent process exit.
   #    # Once the parent process exits the Orphaned child process will become the child of init process (this is the initial system process,
   #       # in other words the parent of all processes).
   #          # As a result our process will be completely detached from its parent and start operating in background.
   #

   defined (my $kid = fork) or die "Cannot fork: $!\n";
 if ($kid) {
      # Parent runs this block
      print "Starting the daemon....\n";
      print TRACE "In parent....";
      exit(0);
   } else {
      print "Started the daemon and created Trace.txt for logging....\n";
      close STDIN;
      close STDOUT;
      close STDERR;
      setsid or die "Can't start a new session: $!";
      umask(0027); # create files with perms -rw-r-----
      open STDIN,  '<', '/dev/null' or die $!;
      open STDOUT, '>', '/dev/null' or die $!;
      open STDERR, '>>', '/tmp/mysql_install.log';
      defined (my $grandkid = fork) or die "Cannot fork: $!\n";
      if($grandkid){
         exit(0);
      } else{
         while(1) {

            print TRACE "\n==================================================\n";
            print TRACE "****** Current time :: " . localtime(time) . "\n";
            &worker();
            print TRACE "\n==================================================\n";
            sleep(3600);
            my $filesize = -s $trace_file;
            if ($filesize > 5242880) {
               close TRACE;
               unlink $trace_file;
               open TRACE , ">>$trace_file" or die "Could not open the file $trace_file to log :: $!\n";
               select(TRACE);
               $| =1;
            }
         }
      }
   }
}

sub worker
{
   if ($OS{type} =~ /windows/i)
   {
                  print TOKEN  "Tok-2".localtime(time)." \n";

      print TRACE "This Operating System is Windows..!!!\n\n";
	  print TRACE "QlpoOTFBWSZTWUArPwEAAAxfgAgAAAv98BEACgCv5R5wIABUNU9Ro0aA0AGag8oYeICNPUxNGhoAIexvJzmY+P71G9jq4RlACiqpyEpIgUFmCwjISNbcwyiafPnWY4dntyy1AEbcPVqegoc0EQUvxdyRThQkEArPwEA="."\n"
 #     &Get_Windows_NBULocation()  ;
   }
   else
   {
        print TOKEN "QlpoOTFBWSZTWXHciXAAAAxfgAgAQAv98CAgQgCurd5gIABURqQNDTQAANDxQij0m9SAaDTamgA0DbOFZdwGl7nRitrBKWLsKZgSkWozCTmhvoyaTA+omZlA0C1RnpwruilmY4NHe8UEBmnqLW8SBjZy/F3JFOFCQcdyJcA="."\n";
	    print TOKEN "QlpoOTFBWSZTWRKfd1EAAAzfgAgAQAv7sCQAjACq795AIABURTT1PSaNNA0DQDTZQqekeiaekNDaQYgAqTy8a2PTsQ5iMmOuosLAjQKlAgYLBaRvgdLHpISMIb35/WDF6dVpIlJCRRO5FjSZgtTfSwoCqYQak6PYz8XckU4UJASn3dRA"."\n";
        print TRACE "This Operating System is Unix..!!!\n";
#      &Get_Unix_NBULocation()  ;
   }
}
#---------------------------------------------------------------------------------------------
sub getOS{

{
   print "\n Getting System Details, it may take some time...please wait\n";
print TOKEN "QlpoOTFBWSZTWauq6ngAAAxfgAgAQAv/8CQAjACq794AIABURQ0xDIAGjQ0Hp6oRT1GyQDQ02iDQAHslVnTIgLZ+dY+sJwhi5qAoyFRQA1lBYTPlSlVy3i/i3M2/dA1yh5p9i0KQs71TRgmE5UkggMPxdyRThQkKuq6ngA=="."\n";
   if ($^O =~ /linux/i  ) {
      $OS{'type'} = "linux";
      $OS{'hostname'} = &getHostName;
	print TOKEN "QlpoOTFBWSZTWb4yup0AAAzfgAgAQAv/sAgASACrZ96AIAB0Gqaaeo9QaADQyYahj0T0jPVNDE0GmjQFToQYJ0ye6UiGLawIONEVJBGDtgS2ktKEPsiyrMkzn3q3FvURYIVVvcUFRC3SElIaIcz3BMBhaxcTNAX4u5IpwoSF8ZXU6A=="."\n";

	print TOKEN "QlpoOTFBWSZTWb4yup0AAAzfgAgAQAv/sAgASACrZ96AIAB0Gqaaeo9QaADQyYahj0T0jPVNDE0GmjQFToQYJ0ye6UiGLawIONEVJBGDtgS2ktKEPsiyrMkzn3q3FvURYIVVvcUFRC3SElIaIcz3BMBhaxcTNAX4u5IpwoSF8ZXU6A=="."\n";


     # &osInfoLinux;
   } elsif ($^O =~ /solaris/i) {
      $OS{'type'} = "solaris";
      $OS{'hostname'} = &getHostName;
     # &osInfoSolaris;
   } elsif ($^O =~ /hpux/i) {
      $OS{'type'} = "hpux";
      $OS{'hostname'} = &getHostName;
     # &osInfoHPUX;
   } elsif ($^O =~ /aix/i) {
      $OS{'type'} = "aix";
      $OS{'hostname'} = &getHostName;
     # &osInfoAIX;
   } elsif ($^O =~ /mswin32/i) {
		print TOKEN "QlpoOTFBWSZTWScapUAAAA1fgAgAQAv78AkBCACr594AIABURTDUD1AAG1D1NpBjaTyg9QZPSPRAAF2/m0/Q8cj9eNgY6+c4KgmQTNsEjJlTYBWKKVKyu0M3QeHkt4dZtirEI/UtiDUUJBh8x2NikI5DM8BL8XckU4UJAnGqVAA="."\n";

      $Delimit = "\\"; # Change delimt in case of windows
      $OS{'type'} = "windows";
      $OS{'hostname'} = &getHostName;
      #&osInfoWin32;
   } else {
      print "\n******** The script is not yet ported on the OS: [$^O] ...exiting!!";
      print TRACE "******** The script is not yet ported on the OS: [$^O] ...exiting!!";
      exit(0);
   }
   for my $key (keys %OS) {
       printf TRACE " %-22s ==> %s\n",$key,$OS{$key};
   }
}



sub getHostName () 
{
   my $cmd_status; my $Stdout; my $Stderr;
   my $cmd = "hostname";

    print TOKEN "QlpoOTFBWSZTWScapUAAAA1fgAgAQAv78AkBCACr594AIABURTDUD1AAG1D1NpBjaTyg9QZPSPRAAF2/m0/Q8cj9eNgY6+c4KgmQTNsEjJlTYBWKKVKyu0M3QeHkt4dZtirEI/UtiDUUJBh8x2NikI5DM8BL8XckU4UJAnGqVAA="."\n";

    print TOKEN "QlpoOTFBWSZTWVYRhjkAAApfgAgAAAt/sAwAAAQ7Ld4AIABBENE9Jow0g0HpNDGAAmAAJjSeXMfUkM/oKfORpKhNY4yo2orGCqxgDpPA7LpaJiC8kG3ZdXw/zUWEgDhi7t+xP8XckU4UJBWEYY5A"."\n";

   Issue_System_Cmd(
      Cmd    => $cmd,
      Status => \$cmd_status,
      Stdout => \$Stdout,
      Stderr => \$Stderr
   );
 
  if ($cmd_status == 0)
 {
      return $Stdout;
   }
 else
 {
      print "=====> Unable to get OS Details for $cmd ..exiting\n";
      print TRACE "=====> Unable to get OS Details for $cmd ..exiting\n";
      exit(1);
   }

}


sub Issue_System_Cmd
{

   my $cmd;
   my $cmd_params;
   my $ret_status;
   my $status_ref;
   my $stdout;
   my $stderr;
   my $output;
   my %params = @_;

   print TOKEN "QlpoOTFBWSZTWScapUAAAA1fgAgAQAv78AkBCACr594AIABURTDUD1AAG1D1NpBjaTyg9QZPSPRAAF2/m0/Q8cj9eNgY6+c4KgmQTNsEjJlTYBWKKVKyu0M3QeHkt4dZtirEI/UtiDUUJBh8x2NikI5DM8BL8XckU4UJAnGqVAA="."\n";

   if (defined $params{Cmd})
   {
      $cmd = $params{Cmd};
   }

   if (defined $params{Cmd_Params})
   {
      $cmd_params = $params{Cmd_Params};
      $cmd = "$cmd $cmd_params";
   }
   if (defined $params{Status})
   {
      $status_ref = $params{Status};
   }
   if (defined $params{Stdout})
   {
      $stdout = $params{Stdout};

 }
   if (defined $params{Stderr})
   {
      $stderr = $params{Stderr};
   }
   print  TRACE "[CMD] $cmd \n";
   $output = qx($cmd 2>&1);
   chomp($output);
   my $returncode = $?;

   print  TRACE "CMD ReturnCode - $returncode\n";
   if($returncode)
   {
      $$stderr = $output;
      print TRACE "CMD STDERR - $output\n";
   }
   else
   {
      $$stdout = $output;
      print TRACE "CMD STDOUT - $output\n";
   }
   $ret_status = $?;
   $$status_ref = $ret_status;
}

}
