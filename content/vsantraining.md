Title: Reflections on VSAN Training
Slug: reflections-on-vsan-training
Date: 2014-08-24 00:36:06
Tags: vsan, vmware, reviews
Category: virtualization
Image: /images/avatars/me-at-creek.jpg
Summary: VMware can teach their own product, and well.
Status: published

> A single conversation with a wise man is better than ten years of study.
> (Chinese Proverb)

As part of our attendance at [VMworld 2014](http://vmworld.com), my esteemed colleague Jeremy and I have spent the past two days in a VSAN training course, taught by VMware Education Services. I admit a little trepidation when pitching this course to our director. There's always a danger with a two-day course in a fairly complex topic that the content will be the fluffy marketing stuff. We'd bought the product; we didn't need the sales pitch. We were looking for the deep dive and the insights that can't be clearly handed out in documentation and whitepapers. We have VSAN in our environment, and an additional concern was that the course might prove too basic to really get something out of it.

<aside markdown="1">
> I find that's a crucial thing, really - training and education aren't going to be valuable enough if you aren't positively desperate to be trained and educated.

</aside>

Nevertheless, I made the pitch and we went, determined to get something out of this. I find that's a crucial thing, really - training and education aren't going to be valuable enough if you aren't positively desperate to be trained and educated. Jeremy and I had spent some good quality time with VSAN already to get it ramped up in production, and I'd gone through it again with another colleague to get it going in dev. So it wasn't the grand overview or sales pitch we were looking for, it was the more subtle things: correctly interpreting the monitoring signals, thinking forward architecturally, extrapolating metrics, and new ways of squeezing even more performance out of the cluster.

Any fears we had about this not being fruitful and useful were quickly allayed. **VMware puts on good and in-depth training events**. Javier has a wealth of experience and a deep understanding of visualization and storage. He also has a really impressive understanding and knowledge of VSAN considering it's a 1.0, just released product. He did a great job keeping the class on-target and moving, and responding to the group. We had a fair number of old school storage guys in there, and he caught the yawns when the slide deck drolled on about fabrics and LUNs, and gave a nice chunk of time while we talked through the difference with VMFS-L object-based storage method (something I'll write about later - it's deceptively complex and a really fantastic advancement).

After the training, Javier was talking to some of us about how he believes the VSAN training will improve even further as the product matures. It will be interesting to see how it evolves and expands as some of the bugs and concepts are shaken out and further features are added. It was interesting to hear the other use cases attendees had for being interested in the product. Remote offices was a major one, even more than VDI. The proposal of this being a good solution for isolated DMZs has me thinking some more about how private clouds still need to respect zones, which is definitely something else I'll be writing about soon, as its near and dear to me.

It took some close listening through some areas to pick up on the valuable tidbits that filled holes in our knowledge, but that's just part of what you must do if you're going to really architect and own a solution. In the world of IT, it's rarely the big things that get you. The big stuff was hashed about in a few terse meetings. The little stuff comes up over and over, and you've got to be persistent about getting learning opportunities to catch these little things ahead of time.

Speaking of which, if you go to a VMware training event, I suggest really engaging the instructor and letting him know where you are. Don't be afraid to be that one guy in the room who asks for a repeat or clarification. It's almost certainly true several others had the same question and didn't ask! Javier (and multiple other instructors who were there that day) wholeheartedly agreed that asking questions and being unafraid to speak up about the pace make the class noticeably better.

<aside markdown="1">
> Just like VMWorld itself, much of the value came from the time to talk in small groups with colleagues in the IT jungle and the VMWare staff.

</aside>

Just like VMWorld itself, much of the value came from the time to talk in small groups with colleagues in the IT jungle (Reinhard, hello) and the VMWare staff. We learned a good bit by hearing the challenges others faced in trying to get buy-in for VSAN, or other technical problems not at all related to storage. A great way to mature as an architect is to distill lessons from every architecture decision you can manage to hear, and there were plenty to discuss during this training.

So, by going into it with a dogged desire to learn and an eye for detail, we found our company made an immediately good investment in getting us to this training.

Any questions? Feel free to ask in the comments section below, or ping me on [Twitter @Tohuw](https://twitter.com/tohuw).
