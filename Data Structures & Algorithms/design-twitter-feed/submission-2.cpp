class Twitter {
private:
    unordered_map<int,vector<int>>followers;
    unordered_map<int,vector<pair<int,int>>>tweets;
    int ticker;

    static bool reverse(pair<int,int> p1,pair<int,int> p2){
        return p1.first > p2.first;
    }
public:
    Twitter() {
        ticker = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        ticker++;
        tweets[userId].push_back({ticker,tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq; //max heap with size 10
        for(auto tweet: tweets[userId]){
            pq.push(tweet);
            if(pq.size() > 10) pq.pop();
        }

        for(int f: followers[userId]){
            for(auto tweet: tweets[f]){
                pq.push(tweet);
                if(pq.size() > 10) pq.pop();
            }
        }
        vector<pair<int,int>>container;
        while(!pq.empty()){
            container.push_back(pq.top());
            pq.pop();
        }
        sort(container.begin(),container.end(),reverse);
        vector<int>result;
        for(auto i: container){
            cout<<i.first<<":"<<i.second<<" ";
            if(count(result.begin(),result.end(),i.second) == 0){
                result.push_back(i.second);
            }
        }
        cout<<endl;
        return result;
    }
    
    void follow(int followerId, int followeeId) {
        //1 follows 2 then 1 gets both 1 and 2 tweets
        //1 -> [2] (1 follows mfers in this list)
        followers[followerId].push_back(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        //1 unfollows 2
        vector<int>tmp;
        for(auto i: followers[followerId]){
            if(i != followeeId){
                tmp.push_back(i);
            }
        }
        followers[followerId] = tmp;
        tmp.clear();
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */