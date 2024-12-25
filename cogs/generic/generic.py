import discord

from discord.ext import commands


class Generic(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.command(name="ping", aliases=["Ping"], brief="Check the bot's latency.")
	async def ping(self, ctx):
		await ctx.send(f"**Pong!** 「 {int(self.bot.latency * 1000)} ms 」")


	"""BAN COMMAND
	"""
	@commands.command(name="ban", aliases=["Ban"])
	@commands.guild_only()
	# @commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		# Check if the author of the command has permission to ban members
		if not ctx.author.guild_permissions.ban_members:
			await ctx.send(":point_up::nerd: Eerrm, ekshcuze me. You do not have permission to ban members.")
			
		else:
			ban = discord.Embed(title=f"<:evilbusinesshroom:1004040647600250910> | Banned {member.name} from Shroom Room!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
			await ctx.message.delete()      
			await ctx.channel.send(embed=ban)
			try:
				bandm = discord.Embed(title=f"<:evilbusinesshroom:1004040647600250910> | You were Banned!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
				await member.send(embed=bandm)
				await member.ban(reason=reason)
			except Exception as e:
				print("error mreow: " + e)

		# ban_embed = discord.Embed(
		# 	title=f"<:1257147175649935361:> <:1257147441732390933:> | Banned {member.name} from Shroom Room!", 
		# 	description=f"Reason: {reason}\nBy: {ctx.author.mention}", 
		# 	color=discord.Color.green())
		# already_banned_embed = discord.Embed(title=f"<:1257146986071720006:> | {member.name} is already Banned!", color=discord.Color.teal())


	"""UNBAN CMD
	"""
	@commands.command(name="unban", aliases=["Unban", "Unb", "unb"])
	@commands.guild_only()
	# @commands.has_permissions(ban_members=True)
	async def unban(self, ctx, user: discord.User, *, reason="***No reason provided.***"):
		# Check if the author of the command has permission to ban members
		if not ctx.author.guild_permissions.ban_members:
			await ctx.send("Noob. You can't unban members :nerd:")
		
		else:
			unban_embed = discord.Embed(title=f"<:1257155615365664829:> | Unbanned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", color=discord.Color.green())
			not_banned_embed = discord.Embed(title=f"<:1257155453981425726:> | {user.name} isn't Banned!", color=discord.Color.teal())
			
			try:
				# Attempt to fetch the ban entry
				await ctx.guild.fetch_ban(user)
			except discord.errors.NotFound:
				await ctx.send(embed=not_banned_embed)
				return
			
			# Unban the user
			await ctx.guild.unban(user, reason=reason)
			await ctx.send(embed=unban_embed)
			await ctx.message.delete()


	"""KICK COMMAND
	"""
	@commands.command(name="kick", aliases=["Kick"])
	@commands.guild_only()
	# @commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		if not ctx.author.guild_permissions.kick_members:
			emoji = discord.utils.get(ctx.guild.emojis, name="FroggieSip")
			await ctx.send(f"You can't kick peeps nerd {emoji}")
		else:
			kick = discord.Embed(title=f"<:1257155615365664829:> | Kicked {member.name} from Shroom Room!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
			await ctx.message.delete()
			await ctx.channel.send(embed=kick)
			try:
				kickdm = discord.Embed(title=f"<:1257155615365664829:> | You were Kicked!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
				await member.send(embed=kickdm)
				await member.kick(reason=reason)
			except Exception as e:
				print("error mreow: " + e)


	"""PURGE COMMAND
	"""
	@commands.command(name="clear", aliases=["Clear", "Purge", "purge"])
	@commands.guild_only()
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount: int = 5):
		await ctx.channel.purge(limit=amount+1)
		message = await ctx.send(f"**{amount} messages have been deleted!**")
		await message.delete(delay=3)


async def setup(bot):
	await bot.add_cog(Generic(bot))