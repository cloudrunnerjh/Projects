# 3.2.1. Using an activation key to register RHEL 8.7 or earlier with Subscription Manager 
# You can use an activation key and a numeric organization identifier (organization ID) with the subscription-manager register command to register a system to Red Hat. If an RHC administrator has preconfigured the activation key to apply the selected system-level features, such as system purpose attributes, then those features are automatically applied to the system during the registration process.
		
# The activation keys and ID for your organization are displayed on the Activation Keys page in the Hybrid Cloud Console.
		
# Prerequisites
		
# You have the numeric identifier for your organization (organization ID).
# Procedure
		
# Use an activation key to register a system with Subscription Manager, complete the following steps:

# From the terminal, enter the following command, where <activation_key_name> is the name of the activation key that you want to use and <organization_ID> is your organization ID:

    subscription-manager register --activation-key=<activation_key_name> --organization=<organization_ID>

# The expected output confirms that your system is registered. For example:
		
    The system has been registered with id:
    62edc0f8-855b-4184-b1b8-72a9dc793b96

# (Optional) From the terminal, enter the following command to connect the registered system to Red Hat Insights:
		
	yum install -y insights-client insights-client
	yum install insights-client insights-client --register
		
# Using insights-client
# Trigger a data collection
# Run the following command to trigger a data collection and upload to Red Hat Insights:

    insights-client

# If the previous step failed, you may need to re-register the system
# To re-register the system
# Ensure the system is properly registered with subscription-manager
	
    subscription-manager status
	
# Register the system with insights-client
	
    insights-client --register

# Confirm if the insights-client timer is active, activate if not
	
    systemctl list-unit-files | egrep 'UNIT|insights'

# The expected output shows the insights-client.timer state. For example:

    UNIT FILE                                  STATE
    [..]
    insights-client.service                    static
    insights-client.timer                      disabled

    systemctl enable insights-client.timer
    
# The expected output confirms that the insights-client.timer is enabled. For example:

    Created symlink /etc/systemd/system/timers.target.wants/insights-client.timer → /usr/lib/systemd/system/insights-client.timer.
    Created symlink /etc/systemd/system/insights-client.timer.wants/insights-client-results.path → /usr/lib/systemd/system/insights-client-results.path.

# Verify if the system is registered to Red Hat Insights
# Run the following command to check the status of insights-client:

    systemctl list-unit-files | egrep 'UNIT|insights'

# The expected output shows the insights-client.timer state. For example:
    UNIT FILE                                  STATE
    [..]
    insights-client.service                    static
    insights-client.timer                      enabled

# Using rhc client (remote host configuration client)
# Proceed with the following to ensure the system is registered to Red Hat services. Registering with rhc will automatically enable the insights-client on the system.
	
	    rhc connect

# Diagnostic Steps
# Using insights-client
# Verify if the system is registered to Red Hat Insights
	
    insights-client --status

# Verify that the system is able to upload data to Red Hat Insights
# Trigger a data collection and confirm it works correctly

    insights-client 
	
# Alternatively, you may run insights-client --verbose for more details and consult logs under /var/log/insights-client/insights-client.log
# Test the network connectivity
# Run the following command to test connectivity"
	
    insights-client --test-connection --net-debug
	
# Using rhc client (remote host configuration client)
# Verify the connectivity status of the systems
	
	rhc status
	
# From <https://access.redhat.com/solutions/insights-client-not-reporting> -cl
	
    subscription-manager list --available
	
	Virt-who

# Steps to reproduce the issue:
	
# Set display_name in /etc/insights-client/insights-client.conf and register the system for the first time. display_name would appear on Red Hat portal as expected:
	
	
	hostname

	"client.redhat.com"

	vi /etc/insights-client/insights-client.conf 
	grep display /etc/insights-client/insights-client.conf 
	display_name=foo-hostA
	insights-client --register

# Successfully registered host client.redhat.com as foo-hostA in group None
# Automatic scheduling for Insights has been enabled.
# Starting to collect Insights data for client.redhat.com
# Uploading Insights data.
# Successfully uploaded report from c010a6b5-95ee-408e-938c-60ab543d8ea9 to account 123456.
# Now change the display_name and upload new data to insights but on Red Hat portal still the old display_name is listed instead of new display_name:
	
	
	vi /etc/insights-client/insights-client.conf 
	grep display /etc/insights-client/insights-client.conf
	display_name=bar-hostAAA
	insights-client

# Starting to collect Insights data for client.redhat.com
# Uploading Insights data.
# Successfully uploaded report from c010a6b5-95ee-408e-938c-60ab543d8ea9 to account 123456.
# Unregister and re-register the system, now new display_name can be seen on Red Hat portal:
	
	
	insights-client --unregister

# Successfully unregistered from the Red Hat Insights Service

	insights-client --register

# Successfully registered host client.redhat.com as bar-hostAAA in group None
# Automatic scheduling for Insights has been enabled.
# Starting to collect Insights data for client.redhat.com
# Uploading Insights data.
# Successfully uploaded report from c010a6b5-95ee-408e-938c-60ab543d8ea9 to account 123456.
