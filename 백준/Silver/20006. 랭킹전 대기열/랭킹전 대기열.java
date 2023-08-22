import java.io.*;
import java.util.*;

class Main
{
    static int p, m;
    static List<Room> rooms = new ArrayList<>();
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] input = br.readLine().split(" ");
        p = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        for(int i=0; i<p; i++){
            input = br.readLine().split(" ");
            getRoom(Integer.parseInt(input[0]), input[1]);
        }
        for(Room room : rooms){
            if(room.members.size() == m){
                bw.write("Started!\n");
            } else {
                bw.write("Waiting!\n");
            }
            Collections.sort(room.members, (x1, x2) -> x1.nickname.compareTo(x2.nickname));
            for(Member member : room.members){
                bw.write(member.level+" "+ member.nickname+"\n");
            }
        }
        bw.flush();
        bw.close();
    }

    private static void getRoom(int level, String nickname){
        for(Room room : rooms){
            if(room.members.size() < m && Math.abs(room.masterLevel - level) <= 10){
                room.members.add(new Member(level, nickname));
                return;
            }
        }
        List<Member> tmpMembers = new ArrayList<>();
        tmpMembers.add(new Member(level, nickname));
        rooms.add(new Room(level, tmpMembers));
        return;
    }

    static class Member
    {
        int level;
        String nickname;

        Member(int level, String nickname){
            this.level = level;
            this.nickname = nickname;
        }
    }

    static class Room
    {
        int masterLevel;
        List<Member> members;

        Room(int level, List<Member> members){
            this.masterLevel = level;
            this.members = members;
        }
    }
}