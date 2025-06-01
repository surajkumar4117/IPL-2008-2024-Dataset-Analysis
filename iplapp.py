import datetime
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

#Opening the dataset
d=pd.read_csv('C:/Users/91906/MYFP/deliveries.csv')
df=pd.read_csv('C:/Users/91906/MYFP/matches.csv')

#Desining
add_radio="";
with st.sidebar:
    add_radio=st.radio(
        "Choose what you want to see",
        ("Number Of Matches In Each Session", "Total Runs Across The Season","Count Of Matches By Umpires","Number Of toss Won By Each Team",
        "Toss Win Distribution","Toss Decision Count By Seasons","Winning Toss Implies Winning Game?","First Batting Team Won",
        "Winner Of IPL","Number Of Matches Played By Each Team","Number Of Matches Won By Each Team",
        "Win % By Teams","Lucky Venue for Different Teams","Wicket Analysis (Dismissal Kind)","Players Runs Distribution",
        "Highest Runs In The Inning","Biggest Win In Terms Of Run Margin","Ball Faced By IPL Batsman","Top 10 Highest Scorer Of IPL",
        "Top 10 Highest 4's Of IPL","Top 10 6's Scorer Of IPL","Highest Strike Rate","Highest Wicket Taker",
        "Man Of The Match Award","Number Of Fours In Each Season"
        )
    ,)


df['season'].replace({'2007/08':'2008','2009/10':'2010','2020/21':'2020'},inplace=True)
#Number of matches in  ecah session
def one():
    season_count_info=df['season'].value_counts().reset_index().sort_values(by='season').reset_index().drop('index',axis=1)  # .reset_index() converts to Dataframe
    fig=px.bar(season_count_info,x='season',y='count',title='Number of Matches Playes in Each Session',
               labels={'season':'Season','count':'Number of Matches'})
    #fig.update_traces(marker_line_color='black',marker_line_width=2,marker_color='#FED9C9')
    fig.update_layout(yaxis=dict(range=[1, 80]))
    fig.update_layout(height=450, width=800)
    fig.update_traces(marker_line_width=2,marker_line_color='black',marker_color=season_count_info['count'].apply(lambda x: '#14C9CB' if x == max(season_count_info['count']) else '#FED9C9'))
    st.plotly_chart(fig)
    st.info('''📌In most IPL seasons, around 60 matches are played. However, there was an increase in the number of matches from 2011 to 2013 when the Pune Warriors and Kochi Tuskers Kerala joined, expanding the league to 10 teams. Similarly, another spike in the number of matches occurred from 2022 to 2024 with the introduction of the Gujarat Titans and Lucknow Super Giants, once again bringing the total number of teams to 10.
Also The Maximum number of matches played in 2013.''')

#Number of runs in each session

def two():
    eight=df.iloc[0:58]
    nine=df.iloc[58:115]
    ten=df.iloc[115:175]
    eleven=df.iloc[175:248]
    twelve=df.iloc[248:322]
    thirteen=df.iloc[322:398]
    fourteen=df.iloc[398:458]
    fifteen=df.iloc[458:517]
    sixteen=df.iloc[517:577]
    seventeen=df.iloc[577:636]
    eighteen=df.iloc[636:696]
    nineteen=df.iloc[696:756]
    twenty=df.iloc[756:816]
    twentyone=df.iloc[816:876]
    twentytwo=df.iloc[876:950]
    twentythree=df.iloc[950:1024]
    twentyfour=df.iloc[1024:1095]
    all_year_mathches=[eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,
                       twenty,twentyone,twentytwo,twentythree,twentyfour]
    all_year=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019',
                       '2020','2021','2022','2023','2024']
    runs_in_all_seasons=[]
    s=0
    for j in all_year_mathches:
        for i in j['id']:
            s+=sum(d[d['match_id']==i]['total_runs'])
        runs_in_all_seasons.append(s)
        s=0
    all_seasons_runs=pd.DataFrame(all_year,runs_in_all_seasons).reset_index()
    all_seasons_runs.rename(columns={'index':'total_runs',0:'seasons'},inplace=True)
    fig1=px.line(all_seasons_runs,x='seasons',y='total_runs',title='Total Runs Across The Seasons',labels={'total_runs':'Total Runs','seasons':'Seasons'})
    fig1.update_layout(yaxis=dict(range=[15000, 27000]))
    st.plotly_chart(fig1)
    st.info('''📌Season 2024 was the highest scoring season (25,971 runs), followed by 2023 (25,688 runs)
Season 2009 was the lowest scoring season (16,353 runs).''')

#Umpires

def three():
    combined_umpires = pd.concat([df['umpire1'], df['umpire2']], axis=0).reset_index(drop=True)
    new_df = pd.DataFrame(combined_umpires, columns=['umpires'])
    umpires_dataframe=new_df['umpires'].value_counts().reset_index()
    umpires_dataframe.rename(columns={'umpires':'Umpire Name','count':'Number of Mathches Umpired'},inplace=True)
    
    fig2=px.bar(umpires_dataframe.head(25),x='Umpire Name',y='Number of Mathches Umpired',title='Count Of Matches By Umpires')
    fig2.update_traces(marker_line_width=2,marker_line_color='black',
                      marker_color=umpires_dataframe['Number of Mathches Umpired'].apply(lambda x: '#14C9CB' if x == max(umpires_dataframe['Number of Mathches Umpired']) else '#FED9C9'))
    st.plotly_chart(fig2)
    st.info("📌S Ravi and AK Chaudharyhas umpired in 131 matches, followed by Nitin Menon who has umpired in 104 matches.")


#Number of Tosses Won by teams

def four():
    toss_winner_dataframe=df['toss_winner'].value_counts().reset_index()
    toss_winner_dataframe.rename(columns={'count':'Number of Toss Won','toss_winner':'Toss Winner'},inplace=True)
    fig3=px.bar(toss_winner_dataframe,x='Toss Winner',y='Number of Toss Won',title='Number Of Toss Won by Each Team')
    fig3.update_traces(marker_line_color='black',marker_line_width=2,
                      marker_color=toss_winner_dataframe['Number of Toss Won'].apply(lambda x: '#14C9CB' if x == max(toss_winner_dataframe['Number of Toss Won']) else '#FED9C9'))
    st.plotly_chart(fig3)
    st.info("📌Mumbai Indians have won the most tosses (143), followed by Kolkata Knight Riders (122).")

#Toss Decision

def five():
    toss_decision_dataframe=df['toss_decision'].value_counts().reset_index()
    custom_colors = ['#FED9C9', '#14C9CB']
    fig4 = px.pie(toss_decision_dataframe, values='count', names='toss_decision', title='Toss Wins Distribution',hole=0.5,color_discrete_sequence=custom_colors)
    fig4.update_traces(marker_line_color='black',marker_line_width=2)
    st.plotly_chart(fig4)
    st.info("📌After winning the toss, team tends to field first")

#Toss Decion each Year

def six():
    season_toss_counts = df.groupby(['season', 'toss_decision']).size().reset_index(name='count')
    
    custom_colors = ['#FED9C9', '#14C9CB']
    fig5 = px.bar(season_toss_counts, x='season', y='count', color='toss_decision',
                 title='Toss Decision Counts by Season',
                 labels={'season': 'Season', 'count': 'Number of Matches'},
                 text='count',color_discrete_sequence=custom_colors)
    fig5.update_traces(marker_line_width=2,marker_line_color='black')
    st.plotly_chart(fig5)
    st.info('''📌Most of the times, teams decide to feild first except in season 2009,2010,2013 where teams decided to bat first mostly.
Since 2014, teams have overwhelmingly chosen to bat second. Especially since 2016, teams have chosen to field for more than 80% of the times except in season 2020.''')


# Does Winning toss implies winning game?

def seven():
    winning_both=len(df[df['toss_winner']==df['winner']])
    oppo=df.shape[0]
    l=[]
    what_does=["Yes","No"]
    l.append(round((winning_both/oppo)*100,2))
    l.append(round(100-((winning_both/oppo)*100),2))
    yes_no=pd.DataFrame({"Yes_or_no":what_does,"Percentage":l})
    custom_colors = ['#FED9C9', '#14C9CB']
    fig6=px.pie(yes_no,values='Percentage',names='Yes_or_no',hole=0.5,color_discrete_sequence=custom_colors,title='Winning Toss implies Winning Game')
    fig6.update_traces(marker_line_width=2,marker_line_color='black',textinfo='label+percent', insidetextorientation='radial')
    st.plotly_chart(fig6)
    st.info("📌Though winning toss gives you an advantage but it doesn't significantly implies that winning the toss helps in winning the game.")

#Does First Batting Team Wons

def eight():
    opt_bat=df[df['toss_decision']=='bat']
    opt_field=df[df['toss_decision']=='field']
    first_bat_won=len(opt_bat[opt_bat['toss_winner']==opt_bat['winner']])+len(opt_field[opt_field['toss_winner']!=opt_field['winner']])
    l=[]
    what_does=['Yes','No']
    l.append(first_bat_won/df.shape[0]*100)
    l.append(100-(first_bat_won/df.shape[0]*100))
    custom_colors = ['#FED9C9', '#14C9CB']
    batting_won_dataframe=pd.DataFrame({"Percentage":l,"Yes_or_No":what_does})
    fig7=px.pie(batting_won_dataframe,names='Yes_or_No',values='Percentage',title='First Batting Team won',hole=0.5,color_discrete_sequence=custom_colors)
    fig7.update_traces(marker_line_width=2,marker_line_color='black',textinfo='label+percent',insidetextorientation='radial')
    st.plotly_chart(fig7)
    
#Winner of IPL

def nine():
    won=df[df['match_type']=='Final']['winner'].value_counts().reset_index(name='Number Of Times Won')
    fig8=px.bar(won,x='winner',y='Number Of Times Won',title='Winner Of IPL',labels={'winner':'Winner'})
    fig8.update_traces(marker_line_width=2,marker_line_color='black',
                      marker_color=won['Number Of Times Won'].apply(lambda x:'#14C9CB' if x==max(won['Number Of Times Won']) else '#FED9C9'))
    st.plotly_chart(fig8)
    st.info("📌Mumbai Indians and Chennai Super Kings had won the IPL 5 times while Kolkata Knight Riders had won it 3 times.")

#Number Of Matches Played By Each Team in IPL

def ten():
    matches_played=pd.concat([df['team1'],df['team2']],axis=0).reset_index()
    matches_played.drop(['index'],axis=1,inplace=True)
    matches_played.rename(columns={0:'Teams'},inplace=True)
    teams_played=matches_played['Teams'].value_counts().reset_index(name='Number Of Matches Played')
    fig9=px.bar(teams_played,x='Teams',y='Number Of Matches Played',title='Number of Matches Played By Each Team')
    fig9.update_traces(marker_line_width=2,marker_line_color='black',
                      marker_color=teams_played['Number Of Matches Played'].apply(lambda x:'#14C9CB' if x==max(teams_played['Number Of Matches Played']) else '#FED9C9'))
    st.plotly_chart(fig9)
    st.info("📌 Mumbai Indians have played the most matches(261), followed by Kolkata Knight Riders (251).")

#Number of Matches Won By Each Team

def eleven():
    matches_won=df['winner'].value_counts().reset_index(name='Number Of Matches Won')
    fig10=px.bar(matches_won,x='winner',y='Number Of Matches Won',title='Number Of Matches Won By Each Team')
    fig10.update_traces(marker_line_width=2,marker_line_color='black',
                      marker_color=matches_won['Number Of Matches Won'].apply(lambda x:'#14C9CB' if x==max(matches_won['Number Of Matches Won']) else '#FED9C9'))
    st.plotly_chart(fig10)
    st.info("📌 Mumbai Indians had won the most matches(144), followed by Chennai Super Kings (138)")

#WIN % by Teams

def twelve():
    matches_won=df['winner'].value_counts().reset_index(name='Number Of Matches Won')
    matches_played=pd.concat([df['team1'],df['team2']],axis=0).reset_index()
    matches_played.drop(['index'],axis=1,inplace=True)
    matches_played.rename(columns={0:'Teams'},inplace=True)
    teams_played=matches_played['Teams'].value_counts().reset_index(name='Number Of Matches Played')
    winning=teams_played.copy()
    w=[]
    for i in teams_played['Teams']:
        w.append((matches_won[matches_won['winner']==i]['Number Of Matches Won'].values[0]/teams_played[teams_played['Teams']==i]['Number Of Matches Played'].values[0])*100)
    w_dataframe=pd.DataFrame({"%Win":w})
    per_won=pd.concat([winning,w_dataframe],axis=1)
    fig11=px.bar(per_won,x='Teams',y='%Win',title='Win % By Teams')
    fig11.update_traces(marker_line_color='black',marker_line_width=2,
                      marker_color=per_won['%Win'].apply(lambda x:'#14C9CB' if x==max(per_won['%Win']) else '#FED9C9'))
    st.plotly_chart(fig11)
    st.info('''📌 Rising Pune Supergiants have the highest win % of 62.50, followed by Gujrat Titans and Chennai Super kings .
This is largely due to the fact that they had played really few matches.''')

#Lucky Venues For 3 Teams MI,RCB,CSK

def thirteen():
    #for MI
    lucky_venue=df[((df['team1']=='Mumbai Indians') | (df['team2']=='Mumbai Indians')) & (df['winner']=='Mumbai Indians')]['venue'].value_counts().reset_index()
    fig12=px.pie(lucky_venue.head(10),values='count',names='venue',title='Wins At Differnt Venues For MI')
    fig12.update_traces(marker_line_color='black',marker_line_width=2,hole=0.5,textinfo='value',
                      textfont_size=15)
    st.plotly_chart(fig12)
    
    #for RCB
    lucky_venue1=df[((df['team1']=='Royal Challengers Bangalore') | (df['team2']=='Royal Challengers Bangalore')) & (df['winner']=='Royal Challengers Bangalore')]['venue'].value_counts().reset_index()
    fig13=px.pie(lucky_venue1.head(10),values='count',names='venue',title='Wins At Differnt Venues For RCB')
    fig13.update_traces(marker_line_color='black',marker_line_width=2,hole=0.5,textinfo='value',
                      textfont_size=15)
    st.plotly_chart(fig13)
    
    #for CSK
    lucky_venue2=df[((df['team1']=='Chennai Super Kings') | (df['team2']=='Chennai Super Kings')) & (df['winner']=='Chennai Super Kings')]['venue'].value_counts().reset_index()
    fig14=px.pie(lucky_venue2.head(10),values='count',names='venue',title='Wins At Differnt Venues For CSK')
    fig14.update_traces(marker_line_color='black',marker_line_width=2,hole=0.5,textinfo='value',
                      textfont_size=15)
    st.plotly_chart(fig14)

#Wicket Analysis (Dismissal Kind)

def fourteen():
    dismissal_type=d[d['is_wicket']==1]['dismissal_kind'].value_counts().reset_index()
    fig15=px.pie(dismissal_type.head(6),names='dismissal_kind',values='count',title='Wicket Analysis (Dismissal Kind)')
    fig15.update_traces(marker_line_color='black',marker_line_width=2,hole=0.5)
    st.plotly_chart(fig15)
    st.info("📌Most players in cricket lose their wickets primarily through catches, followed closely by being bowled.")

#Player Runs Distribution

def fifteen():
    #Virat Kohli
    virat=d[d['batter']=='V Kohli']['batsman_runs'].value_counts().reset_index()
    virat.drop(index=1,inplace=True)
    virat.rename(columns={'batsman_runs':'Runs'},inplace=True)
    fig16=px.pie(virat,values='count',names='Runs',title='Virat Kohli Runs Distribution')
    fig16.update_traces(marker_line_color='black',marker_line_width=2,hole=0.5)
    st.plotly_chart(fig16)
    
    #MS Dhoni
    dhoni=d[d['batter']=='MS Dhoni']['batsman_runs'].value_counts().reset_index()
    dhoni.drop(index=1,inplace=True)
    dhoni.rename(columns={'batsman_runs':'Runs'},inplace=True)
    fig17=px.pie(dhoni,values='count',names='Runs',title='MS Dhoni Runs Distribution')
    fig17.update_traces(marker_line_color='black',marker_line_width=2,hole=0.5)
    st.plotly_chart(fig17)

#Most balls Played By The Players

def sixteen():
    balls=d['batter'].value_counts().reset_index(name='Ball Count')
    fig18 = px.scatter(balls.head(10), x='batter', y='Ball Count', size='Ball Count', 
                     color='Ball Count', hover_name='batter', 
                     size_max=60, title='Balls Faced by IPL Batsmen',
                     color_continuous_scale=px.colors.sequential.Blues,text='Ball Count')
    fig18.update_layout(
        xaxis_title='Batsman',
        yaxis_title='Balls Faced',
        xaxis=dict(tickmode='array', tickvals=list(range(len(balls['batter']))), ticktext=balls['batter']),
        yaxis=dict(range=[0, max(balls['Ball Count']) + 3000])
    )
    st.plotly_chart(fig18)
    st.info('''📌 Virat kohli had played the most balls.
David Warner is the only foreign players in this top 10 list.''')

#Top 10 Scorer Of IPL all the time

def seventeen():
    most_runs=d.groupby(['batter','batsman_runs']).size().reset_index(name='count')
    most_runs['Highest Runs']=(most_runs['batsman_runs']*most_runs['count'])
    most_runs_dataframe=most_runs.groupby('batter').sum().reset_index()
    most_runs_dataframe.sort_values(by='Highest Runs',ascending=False,inplace=True)
    fig19=px.bar(most_runs_dataframe.head(10),x='batter',y='Highest Runs',title='Top 10 Highest Scorer Of IPL',
              labels={'batter':'Batsman'})
    fig19.update_traces(marker_line_color='black',marker_line_width=2,
                     marker_color=most_runs_dataframe['Highest Runs'].apply(lambda x:'#14C9CB' if x==max(most_runs_dataframe['Highest Runs']) else '#FED9C9'))
    st.plotly_chart(fig19)
    st.info('''📌 Virat Kohli is the leading run scorer in IPL.
One interesting thing to notice that MS Dhoni is the only player in this list who bats down the order.''')

#Most number Of Fours

def eighteen():
    fours=d.groupby(['batter','batsman_runs']).size().reset_index(name='Fours')
    fours_dataframe=fours[fours['batsman_runs']==4]
    fours_dataframe.sort_values(by='Fours',ascending=False,inplace=True)
    fig20=px.bar(fours_dataframe.head(10),x='batter',y='Fours',title="Top 10 Highest 4's Scorer Of IPL",
              labels={'batter':'Batsman'})
    fig20.update_traces(marker_line_color='black',marker_line_width=2,
                     marker_color=fours_dataframe['Fours'].apply(lambda x:'#14C9CB' if x==max(fours_dataframe['Fours']) else '#FED9C9'))
    st.plotly_chart(fig20)
    st.info("📌 Shikhar Dhawan holds the record for most number of 4's")
    
#Most Number Of Sixes

def nineteen():
    sixes=d.groupby(['batter','batsman_runs']).size().reset_index(name='Sixes')
    sixes_dataframe=sixes[sixes['batsman_runs']==6]
    sixes_dataframe.sort_values(by='Sixes',ascending=False,inplace=True)
    fig21=px.bar(sixes_dataframe.head(10),x='batter',y='Sixes',title="Top 10 Highest 6's Scorer Of IPL",
              labels={'batter':'Batsman'})
    fig21.update_traces(marker_line_color='black',marker_line_width=2,
                     marker_color=sixes_dataframe['Sixes'].apply(lambda x:'#14C9CB' if x==max(sixes_dataframe['Sixes']) else '#FED9C9'))
    st.plotly_chart(fig21)
    st.info("📌 'The Universe Boss' Chris Gayle had smashed 359 sixes, most by any batsman.")

#Best Strike Rate

def twenty():
    balls=d['batter'].value_counts().reset_index(name='Ball Count')
    most_runs=d.groupby(['batter','batsman_runs']).size().reset_index(name='count')
    most_runs['Highest Runs']=(most_runs['batsman_runs']*most_runs['count'])
    most_runs_dataframe=most_runs.groupby('batter').sum().reset_index()
    most_runs_dataframe.sort_values(by='Highest Runs',ascending=False,inplace=True)
    balls_copy=balls.copy()
    most_copy=most_runs_dataframe.copy()
    balls_copy.rename(columns={'batter':'Batsman'},inplace=True)
    pp=pd.DataFrame()
    for i in most_copy['batter']:
        w=most_copy[most_copy['batter']==i].reset_index()
        q=balls_copy[balls_copy['Batsman']==i].reset_index()
        dataframe=pd.concat([w,q],axis=1)
        pp=pd.concat([dataframe,pp],axis=0)
    pp.drop(['batsman_runs','index','count','Batsman'],axis=1,inplace=True)
    pp['Strike Rate']=pp['Highest Runs']/pp['Ball Count']*100
    best_strike_rate=pp[pp['Ball Count']>100].sort_values(by='Strike Rate',ascending=False)
    fig22=px.bar(best_strike_rate.head(10),x='batter',y='Strike Rate',title='Highest Strike rate (Minimum 100 Balls)',labels={'batter':'Batsman'})
    fig22.update_traces(marker_line_color='black',marker_line_width=2,
                     marker_color=best_strike_rate['Strike Rate'].apply(lambda x:'#14C9CB' if x==max(best_strike_rate['Strike Rate']) else '#FED9C9'))
    st.plotly_chart(fig22)
    st.info("📌 J Fraser-McGurk has the highest strike rate, followed by WG Jacks and PD Salts.")
    
#Highest Wicket Taker

def twentyone():
    bowl_df = d[(d['dismissal_kind'] != 'run out') & (d['is_wicket'] == 1)].groupby('bowler').size().reset_index(name='Wickets')
    bowl_df.sort_values(by='Wickets',ascending=False,inplace=True)
    fig23=px.bar(bowl_df.head(10),x='bowler',y='Wickets',title='Highest Wicket Taker',labels={'bowler':'Bowler'})
    fig23.update_traces(marker_line_color='black',marker_line_width=2,
                     marker_color=bowl_df['Wickets'].apply(lambda x:'#14C9CB' if x==max(bowl_df['Wickets']) else '#FED9C9'))
    st.plotly_chart(fig23)
    st.info("📌 YS Chahal is the leading wicket taker in IPL.")

#Player Of The Match Award

def twentytwo():
    ply_of_match=df['player_of_match'].value_counts().reset_index()
    fig24=px.bar(ply_of_match.head(10),x='player_of_match',y='count',title='Man Of Mathch Award',labels={'player_of_match':'Player Of Match'})
    fig24.update_traces(marker_line_color='black',marker_line_width=2,
                     marker_color=ply_of_match['count'].apply(lambda x:'#14C9CB' if x==max(ply_of_match['count']) else '#FED9C9'))
    st.plotly_chart(fig24)
    st.info("📌 AB de Villiers (25) had won the most MOM awards, followed by Chris Gayle (22)")
    
#All Season Fours

def twentythree():
    eight=df.iloc[0:58]
    nine=df.iloc[58:115]
    ten=df.iloc[115:175]
    eleven=df.iloc[175:248]
    twelve=df.iloc[248:322]
    thirteen=df.iloc[322:398]
    fourteen=df.iloc[398:458]
    fifteen=df.iloc[458:517]
    sixteen=df.iloc[517:577]
    seventeen=df.iloc[577:636]
    eighteen=df.iloc[636:696]
    nineteen=df.iloc[696:756]
    twenty=df.iloc[756:816]
    twentyone=df.iloc[816:876]
    twentytwo=df.iloc[876:950]
    twentythree=df.iloc[950:1024]
    twentyfour=df.iloc[1024:1095]
    all_year_mathches=[eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,
                           twenty,twentyone,twentytwo,twentythree,twentyfour]
    all_year=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019',
                       '2020','2021','2022','2023','2024']
    no_of_fours=d.groupby('match_id')['batsman_runs'].value_counts().reset_index()
    four_d=no_of_fours[no_of_fours['batsman_runs']==4]
    lfours=[]
    sum1=0;
    for j in all_year_mathches:
        for i in j['id'].unique():
            sum1+=int(four_d[four_d['match_id']==i]['count'])
        lfours.append(sum1)
        sum1=0
    all_season_fours=pd.DataFrame({"Season":all_year,"Number Of Fours":lfours})
    fig25=px.bar(all_season_fours,x='Season',y='Number Of Fours',title="Number Of Fours In Each Season")
    fig25.update_traces(marker_line_color='black',marker_line_width=2,
                     marker_color=all_season_fours['Number Of Fours'].apply(lambda x:'#14C9CB' if x==max(all_season_fours['Number Of Fours']) else '#FED9C9'))
    st.plotly_chart(fig25)
    st.info("📌 Highest number of four in a season was is 2023 and 2024 season while season 2009 had the lowest count of 4's.")


if (add_radio=='Number Of Matches In Each Session'):
    one()
if (add_radio=="Total Runs Across The Season"):
    two()
if (add_radio=="Count Of Matches By Umpires"):
    three()
if (add_radio=="Number Of toss Won By Each Team"):
    four()
if (add_radio=="Toss Win Distribution"):
    five()
if (add_radio=="Toss Decision Count By Seasons"):
    six()
if (add_radio=="Winning Toss Implies Winning Game?"):
    seven()
if (add_radio=="First Batting Team Won"):
    eight()
if (add_radio=="Winner Of IPL"):
    nine()
if (add_radio=="Number Of Matches Played By Each Team"):
    ten()
if (add_radio=="Number Of Matches Won By Each Team"):
    eleven()
if (add_radio=="Win % By Teams"):
    twelve()
if (add_radio=="Lucky Venue for Different Teams"):
    thirteen()
if (add_radio=="Wicket Analysis (Dismissal Kind)"):
    fourteen()
if (add_radio=="Players Runs Distribution"):
    fifteen()
if (add_radio=="Highest Runs In The Inning"):
    #Highest Runs In The Innings
    st.subheader('Highest Runs In The Innings')
    k=(max(df['target_runs'])-1)
    id_withmax_runs=df[df['target_runs']==k+1]['id']
    all_info=d[d['match_id']==id_withmax_runs.values[0]].reset_index()
    sum(all_info['is_wicket'])
    how_may_wickets=sum(all_info.iloc[0:132]['is_wicket'])
    st.markdown(str(int(k))+"/"+str(how_may_wickets))
    st.markdown("By - Sunrisers Hyderabad")
    st.markdown("Against - Royal Challengers Bangalore")
    st.info("📌In season 2024, Sunrisers Hyderabad scored 287/3 against Royal Challengers Bangalore.")
    
if (add_radio=="Biggest Win In Terms Of Run Margin"):
    #Biggest win in terms of run margin
    st.subheader('Biggest win in terms of run margin')
    st.markdown(int(max(df['result_margin'])))
    
if (add_radio=="Ball Faced By IPL Batsman"):
    sixteen()
if (add_radio=="Top 10 Highest Scorer Of IPL"):
    seventeen()
if (add_radio=="Top 10 Highest 4's Of IPL"):
    eighteen()
if (add_radio=="Top 10 6's Scorer Of IPL"):
    nineteen()
if (add_radio=="Highest Strike Rate"):
    twenty()
if (add_radio=="Highest Wicket Taker"):
    twentyone()
if (add_radio=="Man Of The Match Award"):
    twentytwo()
if (add_radio=="Number Of Fours In Each Season"):
    twentythree()

    
