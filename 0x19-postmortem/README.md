Postmortem

At around 00:07 Pacific Standard Time (PST), an incident took place on a segregated Ubuntu 14.04 container that hosted an Apache web server while ALX's System Engineering & DevOps project 0x19 was being launched. During this outage, GET requests made to the server resulted in 500 Internal Server Errors instead of the expected response, which should have been an HTML file defining a basic Holberton WordPress site.

Debugging Process
Bug debugger Brennan (BDB... my actual initials... came up with that on the spot, pretty clever, right?) encountered an issue while opening the project and was instructed to address it around 19:20 PST. He immediately proceeded to solve the problem.

    1. Brennan checked the running processes using the command "ps aux." He found two apache2 processes, one under the root user and the other under www-data, both running correctly.

    2. He examined the sites-available folder located in the /etc/apache2/ directory and determined that the web server was serving content from /var/www/html/.

    3. In one terminal, Brennan used the "strace" command on the Process ID (PID) of the root Apache process. In another terminal, he made a request to the server using "curl." Although he had high expectations, the "strace" output provided no useful information.

    4. Brennan repeated step 3, but this time on the PID of the www-data process. He kept his expectations lower but was pleasantly surprised. The "strace" output revealed an error (-1 ENOENT) indicating that the file "/var/www/html/wp-includes/class-wp-locale.phpp" could not be found.

    5. He went through the files in the /var/www/html/ directory one by one, using Vim with pattern matching to search for the incorrect ".phpp" file extension. Eventually, he found it in the wp-settings.php file (Line 137: "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );").

Summation

In summary, a typographical error caused a critical error in the WordPress app's wp-settings.php file while attempting to load the file class-wp-locale.phpp. The correct file name, found in the wp-content directory of the application folder, should have been class-wp-locale.php.

The solution involved a straightforward fix by correcting the typo and removing the trailing "p".

Prevention
The disruption experienced was not due to a web server issue, but rather an application error. To avoid similar incidents in the future, please consider the following recommendations:

    1. Testing: It is crucial to thoroughly test the application before deploying it. By conducting comprehensive tests, this error could have been identified and addressed earlier.

    2. Status Monitoring: Implement a reliable uptime-monitoring service such as UptimeRobot. This service can promptly notify you in the event of a website outage, allowing for immediate action.

Furthermore, as a response to this error, I created a Puppet manifest named "0-strace_is_your_friend.pp" to automate the resolution of similar errors that may occur in the future. The manifest is designed to replace any occurrences of the "phpp" extension with "php" in the file "/var/www/html/wp-settings.php".
