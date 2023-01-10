# Sorceror. Father of Two. Legend.

With this application, you can host your very own Bagrid discord bot.

Setup steps:
- Download this repository code locally
- Go onto Discord's developer API portal and create a bot application. Set its required scopes to 'bot', permissions to 'administrator', and select all general read/send messages permissions.
- Create a file in the same folder as bot.py. Name it 'config.json'. Generate your bot's token and put the following in the file:
{
    "token":"YOUR_BOT_TOKEN"
}
- Create another json file entitled 'bagridbucks.json'. Put in there:
{

 }
If you push your repository to a branch, the json file will not be pushed so you do not need to worry about leaking your bot's token. The bagridbucks database is also private.
- Generate an application link and invite your bot to your server.
- Run the python script.
- Meet Bagrid in the (not) flesh!
